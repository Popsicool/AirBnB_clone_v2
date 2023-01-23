#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy
"""

from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['54.157.170.75', '52.3.251.44']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    do deploy deploy to web server
    """
    try:
        if not (path.exists(archive_path)):
            return False
        # upload to the server
        put(archive_path, '/tmp/')
        # create target directory in server
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

        # uncompress and remove extension
        run('sudo tar -xzf /tmp/\
web_static_{}.tgz -C /data/web_static/\
releases/web_static_{}/'.format(timestamp, timestamp))

        # delete the achieve
        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))
        # change content location
        run('sudo mv /data/web_static/\
releases/web_static_{}/\
web_static/* /data/web_static/\
releases/web_static_{}/'.format(timestamp, timestamp))

        # remove web_static dir
        run('sudo rm -rf /data/web_static/\
releases/web_static_{}/web_static'.format(timestamp))

        # delete sym link
        run('sudo rm -rf /data/web_static/current')

        # add new symbolic link
        run('sudo ln -s /data/web_static/\
releases/web_static_{}/ /data/web_static/current'.format(timestamp))
    except Exception as e:
        return False
    # return True on success
    return True
