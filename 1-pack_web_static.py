#!/usr/bin/python3
""" Function that compress a folder """
from fabric.api import local, env
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['54.160.68.58', '100.25.136.241']


def do_pack():
    """
    Targging project directory into a packages as .tgz
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p ./versions')
    path = './versions/web_static_{}'.format(now)
    local('sudo tar -czvf {}.tgz web_static'.format(path))
    name = '{}.tgz'.format(path)
    if name:
        return name
    else:
        return None
