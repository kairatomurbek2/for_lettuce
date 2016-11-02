import shutil
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.conf import settings
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        db_name = settings.DATABASES['default']['NAME']
        db_copy = db_name + 'template'
        try:
            if os.path.isfile(db_copy):
                print "Template db found! Copying to original db..."
                shutil.copyfile(db_copy, db_name)
                print "Success"
                return
            os.remove(db_name)
        except OSError:
            pass
        print "Template db NOT found. Restoring original db..."
        call_command('restore_db', interactive=False, verbosity=0)

        shutil.copyfile(db_name, db_copy)
        print "Copy database created"
