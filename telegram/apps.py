from django.apps import AppConfig
from config.settings import RUN_POLLING
from time import sleep


class TelegramConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telegram'

    """def ready(self):
        if RUN_POLLING == 'TRUE':
            from telegram.services import start_tg
            sleep(1)
            start_tg()
            print('tg started')
        else:
            print('tg not started')"""
