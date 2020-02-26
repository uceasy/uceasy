from uceasy.adapters import CPU, TRINITY, SPADES
import subprocess


def run_trinity(config, output):
    cmd = [TRINITY, "--config", config, "--output", output, "--cores", CPU]
    return subprocess.run(cmd, check=True)


def run_spades(config, output):
    cmd = [SPADES, "--config", config, "--output", output, "--cores", CPU]
    return subprocess.run(cmd, check=True)
