from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    #activar el signals para que se cree el perfil
    def ready(self):
        import core.signals  # noqa

