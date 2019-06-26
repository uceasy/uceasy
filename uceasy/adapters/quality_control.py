import subprocess
from uceasy.adapters import CPU, ILLUMIPROCESSOR


def run_illumiprocessor(config, input, output):
    cmd = [
        ILLUMIPROCESSOR,
        '--input', input,
        '--output', output,
        '--config', config,
        '--cores', CPU,
    ]
    return subprocess.run(cmd, check=True)
