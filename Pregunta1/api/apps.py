from django.apps import AppConfig
from django.core.cache import cache

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    def ready(self):
        cache.clear()


