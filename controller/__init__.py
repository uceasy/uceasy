import os
import shutil
from getpass import getuser


USER = getuser()

WORKENV = f'/home/{USER}/.uceasy/'
CLEAN_FASTQ = WORKENV + 'data/clean_fastq'
TRINITY_ASSEMBLIES = WORKENV + 'data/trinity_assemblies'


if not os.path.isdir(WORKENV):
    os.mkdir(WORKENV)
else:
    shutil.rmtree(WORKENV)
    os.mkdir(WORKENV)
