from django.apps import AppConfig

class ErrorsAppConfig(AppConfig):
    name = 'djangoerrors.errors'

    def ready(self):
        import djangoerrors.errors.models
