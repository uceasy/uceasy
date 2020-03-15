from subprocess import run, PIPE, DEVNULL
from typing import List


ADAPTERS = {}


def adapter(func):
    ADAPTERS[func.__name__] = func
    return func


def _run_adapter(
    cmd: List[str], capture_output: bool, dir_to_execute: str
) -> List[str]:
    """
    Utilitary runner to be used by the adapters.

    :param cmd              the command passed by the adapter as a list.
    :param capture_output   True if you want to receive the output of the
                            command.
    :param dir_to_execute   execute in a different directory.
    :return:                empty list in case of "capture_output=False",
                            otherwise the lines of the command output as a
                            list. One line of output is one item in the list.
    """
    kwargs = {"cwd": dir_to_execute}

    if capture_output:
        kwargs.update(stdout=PIPE, stderr=DEVNULL, universal_newlines=True)

    cmd_return = run(cmd, **kwargs)

    if capture_output:
        return cmd_return.stdout.strip().splitlines()
    return []


@adapter
def illumiprocessor(
    args_as_list: List[str],
    dir_to_execute: str = None,
    capture_output: bool = False,
) -> List[str]:
    """
    illumiprocessor wrapper. see: https://illumiprocessor.readthedocs.io/en/
    latest/
    provide the illumiprocessor arguments as a list via "args_as_list".
    e.g. ["--input", "raw-fastq", "--output", "clean-fastq"]
    """
    cmd = ["illumiprocessor"] + args_as_list
    return _run_adapter(cmd, capture_output, dir_to_execute)


@adapter
def trinity(
    args_as_list: List[str],
    dir_to_execute: str = None,
    capture_output: bool = False,
) -> List[str]:
    """
    phyluce's trinity wrapper.
    provide the trinity arguments as a list via "args_as_list".
    e.g. ["--contig", "clean-fastq", "--cores", "4"]
    """
    cmd = ["phyluce_assembly_assemblo_trinity", "--clean"] + args_as_list
    return _run_adapter(cmd, capture_output, dir_to_execute)
