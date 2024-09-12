from django.core.management import BaseCommand
from telegram.services import print_hello


class Command(BaseCommand):

    def handle(self, *args, **options):
        print_hello()
