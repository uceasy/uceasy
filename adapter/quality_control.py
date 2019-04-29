import subprocess
from adapter import CPU, TRIMMOMATIC


def run_illumiprocessor(conf_file, input, output):
    cmd = [
        'illumiprocessor',
        '--input', input,
        '--output', output,
        '--config', conf_file,
        '--cores', CPU,
        '--trimmomatic', TRIMMOMATIC
    ]
    return subprocess.run(cmd, check=True)
