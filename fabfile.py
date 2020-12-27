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
