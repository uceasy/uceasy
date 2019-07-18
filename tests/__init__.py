from uceasy.context import Context
import os
import shutil


OUTPUT = os.getcwd() + '/output'

if os.path.isdir(OUTPUT):
    shutil.rmtree(OUTPUT)

os.mkdir(OUTPUT)
