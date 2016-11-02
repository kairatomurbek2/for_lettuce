from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.conf import settings
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            os.remove(settings.DATABASES['default']['NAME'])
        except OSError:
            pass
        call_command('migrate', interactive=False, verbosity=0)

        print "\nLoading all data..."
        call_command('loaddata', 'acceptance_tests/fixtures/test.json')
        print "Success\n"