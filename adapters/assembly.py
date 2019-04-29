import subprocess
import os
from adapter import CPU


def run_trinity(conf_file, output):
    if os.path.isdir(output):
        raise IOError('trinity-assemblies directory already exist!\n' +
                      'Move or remove it before running trinity.')
    cmd = [
        'phyluce_assembly_assemblo_trinity',
        '--conf', conf_file,
        '--output', output,
        '--clean',
        '--cores', CPU
    ]
    return subprocess.run(cmd, check=True)
