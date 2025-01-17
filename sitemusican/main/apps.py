from django.apps import AppConfig


class MainConfig(AppConfig):
    verbose_name = "Музыканты Мира"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        import main.signals
