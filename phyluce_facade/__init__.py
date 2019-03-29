import os
from multiprocessing import cpu_count


# folder to store phyluce outputs
WORKENV = '../../workenv/'
if not os.path.isdir(WORKENV):
    os.mkdir(WORKENV)

TRIMMOMATIC = '~/miniconda3/envs/uceasy/share/trimmomatic/trimmomatic.jar'
CPU = str(cpu_count() - 2)

CLEAN_FASTQ = WORKENV + 'data/clean_fastq'
