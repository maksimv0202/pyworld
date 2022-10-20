"""Django api/ app settings"""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Django application api/ configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
