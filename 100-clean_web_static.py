#!/usr/bin/python3

"""Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean
"""
from fabric.api import *
import os

env.hosts = ['54.157.170.75', '52.3.251.44']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_clean(number=0):
    """
    Dele out of date achieves
    """
    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    # list all achieves
    archives = sorted(os.listdir("versions"))
    for a in range(number):
        archives.pop()

    with lcd("versions"):
        for a in archives:
            local("rm ./{}".format(a))

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
