from django.apps import AppConfig
from config.settings import RUN_SCHEDULE
from time import sleep


class TelegramConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telegram'

    def ready(self):
        if RUN_SCHEDULE == 'TRUE':
            from telegram.services import start_scheduler
            sleep(2)
            start_scheduler()
            print('scheduler started')
        else:
            print('scheduler not started')
