from subprocess import run, PIPE, DEVNULL
from typing import List


ADAPTERS = {}


def adapter(func):
    ADAPTERS[func.__name__] = func
    return func


@adapter
def illumiprocessor(
    args_as_list: List[str],
    dir_to_execute: str = None,
    capture_output: str = False,
) -> List[str]:
    """
    illumiprocessor wrapper. see: https://illumiprocessor.readthedocs.io/en/
    latest/
    provide the illumiprocessor arguments as a list via "args_as_list".
    e.g. ["--input", "raw-fastq", "--output", "clean-fastq"]

    :param args_as_list:    list of arguments to illumiprocessor.
    :param capture_output:  True if you want to receive the output of
                            illumiprocessor.
    :return:                empty list in case of "capture_output=False",
                            otherwise the lines of illumiprocessor output as a
                            list. One line of output is one item in the list.
    """
    cmd = ["illumiprocessor"]
    cmd += args_as_list
    kwargs = {"cwd": dir_to_execute}

    if capture_output:
        kwargs.update(stdout=PIPE, stderr=DEVNULL, universal_newlines=True)

    illumiprocessor_return = run(cmd, **kwargs)

    if capture_output:
        return illumiprocessor_return.stdout.strip().splitlines()
    return []
