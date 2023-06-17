from django.core.management.base import BaseCommand
from myapp.models import Mechanic

class Command(BaseCommand):
    help = 'Frees all the mechanics'

    def handle(self, *args, **options):
        # Prepopulate mechanics
        for i in range(1, 11):
            Mechanic.objects.update(availability=True)

        self.stdout.write(self.style.SUCCESS('Mechanics Freed.'))
