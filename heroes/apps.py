from django.apps import AppConfig
from telegram.services import start_tg

class HeroesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'heroes'

"""    def ready(self):
        start_tg()"""
