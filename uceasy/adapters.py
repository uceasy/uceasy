import subprocess
import os


Adapters = {}


def run(cmd):
    conda_env = os.getenv("UCEASY_PHYLUCE", "phyluce")
    cmd = f"conda run -n {conda_env} " + cmd
    return subprocess.run(cmd, shell=True, capture_output=True)


def match_contigs_to_probes(output, contigs, probes):
    cmd = (
        "phyluce_assembly_match_contigs_to_probes "
        f"--contigs {contigs} "
        f"--probes  {probes} "
        f"--output  {output} "
    )
    return run(cmd)
