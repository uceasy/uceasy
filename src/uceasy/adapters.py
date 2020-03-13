from typing import List


ADAPTERS = {}


def illumiprocessor(args_as_list: List[str], capture_output=False) -> List[str]:
    """
    illumiprocessor wrapper. see: https://illumiprocessor.readthedocs.io/en/latest/
    provide the illumiprocessor arguments as a list via "args_as_list".
    e.g. ["--input", "raw-fastq", "--output", "clean-fastq"]

    :param args_as_list:    list of arguments to illumiprocessor
    :param capture_output:  True if you want to receive the output of illumiprocessor
    :return:                empty list in case of "capture_output=False",
                            otherwise the lines of illumiprocessor output as a list.
                            one line of output is one item in the list.
    """
    pass
