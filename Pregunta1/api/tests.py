from django.test import TestCase
from api.views import patente_a_id, id_a_patente

class APITest(TestCase):
    def test_patente_a_id(self):
        self.assertEqual(patente_a_id("AAAA000"), 1)
        self.assertEqual(patente_a_id("AAAA001"), 2)
        self.assertEqual(patente_a_id("AAAB000"), 1001)

    def test_id_a_patente(self):
        self.assertEqual(id_a_patente(1), "AAAA000")
        self.assertEqual(id_a_patente(2), "AAAA001")
        self.assertEqual(id_a_patente(1001), "AAAB000")

    def test_get_id_endpoint(self):
        response = self.client.get("/api/v1/id/AAAA000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], 1)

    def test_get_patente_endpoint(self):
        response = self.client.get("/api/v1/patente/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["patente"], "AAAA000")

    def test_invalid_patente(self):
        response = self.client.get("/api/v1/id/XYZ000/")
        self.assertEqual(response.status_code, 400)  

    def test_invalid_id(self):
        response = self.client.get("/api/v1/patente/0/")
        self.assertEqual(response.status_code, 400)  
