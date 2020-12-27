from __future__ import unicode_literals
from fabric.api import local
from fabric.context_managers import shell_env

def ssh(service):
    """
    ssh into running service container
    :param service: ['django', 'postgres']
    USAGE: fab ssh:service
    """
    assert service in ['django', 'postgres'], "%s is unrecognized service"
    local('docker-compose exec %s sh' % service)

def reset_db():
    """
    Reset db, migrate and generate fixtures.
    Useful when changing branch with different migrations.
    """
    # schema creation
    local('docker-compose exec django python manage.py reset_db')
    local('docker-compose exec django find . -name \'*.pyc\' -delete')
    local('docker-compose exec django find . -path \'*/migrations/*.py\' -not -name \'__init__.py\' -delete')
    local('docker-compose exec django python manage.py makemigrations')
    local('docker-compose exec django python manage.py migrate')
    local('docker-compose exec django python manage.py import_data') 