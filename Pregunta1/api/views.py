from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.cache import cache

LETRAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def patente_a_id(patente):
    if len(patente) != 7 or not patente[:4].isalpha() or not patente[4:].isdigit():
        return None  

    id_num = sum((LETRAS.index(letra) * (26 ** i)) for i, letra in enumerate(reversed(patente[:4])))
    return id_num * 1000 + int(patente[4:]) + 1

def id_a_patente(id_num):
    if id_num < 1:
        return None

    id_num -= 1
    letras_id, numeros = divmod(id_num, 1000)  
    letras = [LETRAS[(letras_id // (26 ** i)) % 26] for i in range(3, -1, -1)]
    
    return "".join(letras) + f"{numeros:03d}"



@api_view(['GET'])
def get_patente(request, id_num):
    cache_key = f"patente:{id_num}"
    patente = cache.get(cache_key)

    if not patente:
        patente = id_a_patente(id_num)
        if patente is None:
            return Response({"error": "ID fuera de rango"}, status=400)
        cache.set(cache_key, patente, timeout=86400)  

    return Response({"id": id_num, "patente": patente})

@api_view(['GET'])
def get_id(request, patente):
    cache_key = f"id:{patente}"
    id_num = cache.get(cache_key)

    if not id_num:
        id_num = patente_a_id(patente)
        if id_num is None:
            return Response({"error": "Patente inválida o contiene Ñ"}, status=400)
        cache.set(cache_key, id_num, timeout=86400)  

    return Response({"patente": patente, "id": id_num})
