import subprocess
from adapters import CPU, ILLUMIPROCESSOR


def run_illumiprocessor(conf_file, input, output):
    cmd = [
        ILLUMIPROCESSOR,
        '--input', input,
        '--output', output,
        '--config', conf_file,
        '--cores', CPU
    ]
    return subprocess.run(cmd, check=True)
