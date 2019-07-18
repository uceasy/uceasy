import subprocess
from uceasy.adapters import CPU, ILLUMIPROCESSOR


def run_illumiprocessor(input, output, config):
    cmd = [
        ILLUMIPROCESSOR,
        '--input', input,
        '--output', output,
        '--config', config,
        '--cores', CPU,
    ]
    return subprocess.run(cmd, check=True)
