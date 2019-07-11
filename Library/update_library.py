# -*- coding: utf-8 -*-

import shutil,os
from distutils.sysconfig import get_python_lib; 


python_library_dir=get_python_lib()

BASE_DIR = os.path.split(os.path.realpath(__file__))[0]


def update_library(name):
    try:
        shutil.rmtree(python_library_dir+'/'+name+'/')
    except:
        pass

    shutil.copytree(BASE_DIR+'/'+name, python_library_dir+'/'+name+'/')
    print u'更新'+name+u'成功'

    
update_library('TestLibrary')
update_library('RedisLibrary')

# raw_input();