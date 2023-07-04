#!/usr/bin/python3

from fabric.api import *

def deploy():
    local('whoami')
