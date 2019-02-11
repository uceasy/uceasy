import os
from multiprocessing import cpu_count


# folder to store phyluce outputs
WORKENV = '../../workenv/'
if not os.path.isdir(WORKENV):
    os.mkdir(WORKENV)

# illumiprocessor arguments
INPUT = WORKENV + 'data/raw_fastq'
OUTPUT = WORKENV + 'data/clean_fastq'
CPU = str(cpu_count() - 2)
TRIMMOMATIC = '~/miniconda3/envs/uceasy/share/trimmomatic/trimmomatic.jar'
