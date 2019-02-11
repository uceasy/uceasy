import os
from multiprocessing import cpu_count


# folder to store phyluce outputs
WORKENV = '../../workenv/'
if not os.path.isdir(WORKENV):
    os.mkdir(WORKENV)
