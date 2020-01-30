import subprocess
import os


ADAPTERS = dict()


def run(cmd):
    return subprocess.run(cmd, capture_output=True)


def adapter(func):
    ADAPTERS[func.__name__] = func
    return func


@adapter
def match_contigs_to_probes(*args, **kargs):
    cmd = ["phyluce_assembly_match_contigs_to_probes"]

    for arg in args:
        cmd.append(arg)
    for k, v in kargs.items():
        cmd.append([k, v])

    return run(cmd)
