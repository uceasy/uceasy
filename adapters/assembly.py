import subprocess
from adapters import CPU, SCRIPT_TRINITY


def run_trinity(config, output):
    cmd = [
        SCRIPT_TRINITY,
        '--config', config,
        '--output', output,
        '--clean',
        '--cores', CPU
    ]
    return subprocess.run(cmd, check=True)
