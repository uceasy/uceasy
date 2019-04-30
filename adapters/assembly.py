import subprocess
import os
from adapters import CPU, SCRIPT_TRINITY


def run_trinity(conf_file, output):
    if os.path.isdir(output):
        raise IOError('trinity-assemblies directory already exist!\n' +
                      'Move or remove it before running trinity.')
    cmd = [
        SCRIPT_TRINITY,
        '--conf', conf_file,
        '--output', output,
        '--clean',
        '--cores', CPU
    ]
    return subprocess.run(cmd, check=True)
