from django.core.management import BaseCommand
from telegram.services import start_tg


class Command(BaseCommand):

    def handle(self, *args, **options):
        start_tg()
