import subprocess
from adapters import CPU, TRINITY, SPADES


def run_trinity(config, output):
    cmd = [
        TRINITY,
        '--config', config,
        '--output', output,
        # '--clean', This was causing the error: Broken pipe
        # See the issue: https://github.com/faircloth-lab/phyluce/issues/159
        '--cores', CPU
    ]
    return subprocess.run(cmd, check=True)


def run_spades(config, output):
    cmd = [
        SPADES,
        '--config', config,
        '--output', output,
        '--cores', CPU
    ]
    return subprocess.run(cmd, check=True)

