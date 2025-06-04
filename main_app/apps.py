from django.apps import AppConfig


class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'
    
    # listen for signals when user submits a new Trail
    def ready(self):
        import main_app.signals