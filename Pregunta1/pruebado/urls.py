
from django.contrib import admin
from django.urls import path
from api.views import get_patente, get_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/id/<str:patente>/', get_id, name='get_id'),
    path('api/v1/patente/<int:id_num>/', get_patente, name='get_patente'),
]

