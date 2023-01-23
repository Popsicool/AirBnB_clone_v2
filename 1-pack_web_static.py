#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static folder of
your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import date
from time import strftime


def do_pack():
    """ create the compressed file"""
    file = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(file))
        return "versions/web_static_{}.tgz".format(file)

    except Exception as e:
        return None
