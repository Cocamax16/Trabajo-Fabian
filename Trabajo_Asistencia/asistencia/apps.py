from django.apps import AppConfig


class AsistenciaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'asistencia'

    def ready(self):
        try:
            from .crear_admin import crear_admin
            crear_admin()
        except Exception as e:
            print(f"Error creando admin: {e}")
