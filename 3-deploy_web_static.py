#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy

"""
import os.path
from fabric.api import put
from fabric.api import run
from datetime import datetime
from fabric.api import env
from fabric.api import local

env.hosts = ['54.157.170.75', '52.3.251.44']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """
    create achieve file (tzr)
    """
    when = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(when.year,
                                                         when.month,
                                                         when.day,
                                                         when.hour,
                                                         when.minute,
                                                         when.second)
    if os.path.isdir("versions") is False:
        # if version directory is not present, create
        if local("mkdir -p versions").failed is True:
            # if unable to create
            return None
        # create the tar file in that directory
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        # if it fail, return
        return None
    return file


def do_deploy(archive_path):
    """
    deploy to the server
    """
    if os.path.isfile(archive_path) is False:
        # if no archieve file
        return False
    file = archive_path.split("/")[-1]
    # extract name from file, remove the .tzr extention
    name = file.split(".")[0]
    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        # push to server but if it fail, return
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """Do the deployment"""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
