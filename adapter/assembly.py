import subprocess
import os
from adapter import WORKENV, CPU

# Trinity arguments
OUTPUT = WORKENV + 'data/trinity_assemblies'


def run_trinity(conf_file):
    if os.path.isdir(OUTPUT):
        raise IOError('trinity-assemblies directory already exist!\n' +
                      'Move or remove it before running trinity.')
    cmd = [
        'phyluce_assembly_assemblo_trinity',
        '--conf', conf_file,
        '--output', OUTPUT,
        '--clean',
        '--cores', CPU
    ]
    return subprocess.run(cmd, check=True)
