from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field: str = "django.db.models.BigAutoField"
    name = "app"
