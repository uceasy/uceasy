import subprocess
from adapters import CPU, ILLUMIPROCESSOR, TRIMMOMATIC


def run_illumiprocessor(conf_file, input, output):
    cmd = [
        ILLUMIPROCESSOR,
        '--input', input,
        '--output', output,
        '--config', conf_file,
        '--cores', CPU,
        '--trimmomatic', TRIMMOMATIC
    ]
    return subprocess.run(cmd, check=True)
