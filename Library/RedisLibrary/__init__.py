#!/usr/bin/python
#coding: utf-8

from manager import RedisManager
from version import VERSION


_version_ = VERSION
 
class RedisLibrary(RedisManager):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
