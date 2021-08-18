r"""Adapters is a dictionary to call command-line programs.

Specify the program with the dictionary key and its arguments as a list.
e.g. adapters["program"](["arg1", "arg2"])
"""

from subprocess import run
from time import time, gmtime, strftime
from typing import List, Dict, Any
from collections import namedtuple


CommandResult = namedtuple("CommandResult", ["command", "stdout", "execution_time"])


TEMPLATES = {
    "illumiprocessor": "illumiprocessor",
    "trinity": "phyluce_assembly_assemblo_trinity",
    "spades": "phyluce_assembly_assemblo_spades",
    "match_contigs_to_probes": "phyluce_assembly_match_contigs_to_probes",
    "get_match_counts": "phyluce_assembly_get_match_counts",
    "get_fastas_from_match_counts": "phyluce_assembly_get_fastas_from_match_counts",
    "explode_get_fastas_file": "phyluce_assembly_explode_get_fastas_file",
    "secap_align": "phyluce_align_seqcap_align",
    "gblocks": "phyluce_align_get_gblocks_trimmed_alignments_from_untrimmed",
    "remove_locus_name_from_nexus_lines": "phyluce_align_remove_locus_name_from_nexus_lines",
    "get_only_loci_with_min_taxa": "phyluce_align_get_only_loci_with_min_taxa",
    "nexus_to_raxml": "phyluce_align_format_nexus_files_for_raxml",
}


class Adapters:
    """Creates a dictionary to run the phyluce programs."""

    def __init__(self):
        self.adapters = dict()
        for key, val in TEMPLATES.items():
            self.add(key, val)

    def add(self, name: str, executable: str) -> None:
        """Add new adapter to the dictionary."""

        def func(args_as_list: List[str]) -> CommandResult:
            """Provide the adapter arguments as a list via "args_as_list"."""
            cmd = [executable] + args_as_list
            return self._run(cmd)

        self.adapters[name] = func

    def _run(self, cmd: List[str]) -> CommandResult:
        """
        Utilitary runner to be used by the adapters.

        :param cmd              the command passed by the adapter as a list.
        :return:                CommandResult tuple containing information like standard output
                                and execution time.
        """
        kwargs: Dict[str, Any] = {
            "capture_output": True,
            "universal_newlines": True,  # receive as string not bytes
        }
        try:
            start_time = time()
            cmd_return = run(cmd, **kwargs)
            exec_time = strftime("%H:%M:%S", gmtime(time() - start_time))
            return CommandResult(cmd, cmd_return.stdout.strip().splitlines(), exec_time)
        except FileNotFoundError:
            print(f"ERROR: Couldn't find {cmd[0]}, is phyluce installed?")
            exit(1)
