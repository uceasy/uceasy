import subprocess
import os
import shutil
from uceasy.adapters import CPU, ILLUMIPROCESSOR


def run_illumiprocessor(input, output, config):

    # Prevent Illumiprocessor from asking to remove output dir
    if os.path.isdir(output):
        shutil.rmtree(output)

    cmd = [
        ILLUMIPROCESSOR,
        "--input",
        input,
        "--output",
        output,
        "--config",
        config,
        "--cores",
        CPU,
    ]
    return subprocess.run(cmd, check=True)
