import subprocess
from adapters import CPU, ILLUMIPROCESSOR, TRIMMOMATIC


def run_illumiprocessor(config, input, output):
    cmd = [
        ILLUMIPROCESSOR,
        '--input', input,
        '--output', output,
        '--config', config,
        '--cores', CPU,
        '--trimmomatic', TRIMMOMATIC
    ]
    return subprocess.run(cmd, check=True)
