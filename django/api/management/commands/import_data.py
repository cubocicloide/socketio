from __future__ import absolute_import

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command
from api.models import User


class Command(BaseCommand):
    help = 'Creates a set of ORM objects for development and staging environment.'

    def handle(self, *args, **options):    
        admin, created = User.objects.get_or_create(email='admin@example.com', defaults={
            'username': 'admin@example.com',
            'is_superuser': True,
            'is_staff': True,
        })
        password = 'Passw0rd!'
        admin.set_password(password)
        admin.save()
        print('Superuser {}: {}/{}'.format('created', admin.email, password))
        self.stdout.write("Fake data script done.")
