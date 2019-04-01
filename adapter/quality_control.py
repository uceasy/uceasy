import subprocess
from adapter import WORKENV, CPU, TRIMMOMATIC

# illumiprocessor arguments
INPUT = WORKENV + 'data/raw_fastq'
OUTPUT = WORKENV + 'data/clean_fastq'


def run_illumiprocessor(conf_file):
    cmd = [
        'illumiprocessor',
        '--input', INPUT,
        '--output', OUTPUT,
        '--config', conf_file,
        '--cores', CPU,
        '--trimmomatic', TRIMMOMATIC
    ]
    return subprocess.run(cmd, check=True)
