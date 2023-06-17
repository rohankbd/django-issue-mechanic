from django.core.management.base import BaseCommand
from myapp.models import Mechanic

class Command(BaseCommand):
    help = 'Prepopulates the database with initial data'

    def handle(self, *args, **options):
        # Prepopulate mechanics
        for i in range(1, 11):
            Mechanic.objects.create(mechanicID=i)

        self.stdout.write(self.style.SUCCESS('Database prepopulation complete.'))
