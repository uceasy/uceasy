r"""Adapters is a dictionary to call command-line programs.

Specify the program with the dictionary key and its arguments as a list.
e.g. adapters["program"](["arg1", "arg2"])
"""

from subprocess import run, PIPE
from time import time, gmtime, strftime
from typing import List, Dict, Any
from collections import namedtuple


CommandResult = namedtuple("CommandResult", ["command", "stdout", "execution_time"])


# Command names target PHYLUCE 1.7 (Python 3). Notable renames from 1.6:
#   - Trinity assembler was removed upstream in 1.7.
#   - phyluce_align_remove_locus_name_from_nexus_lines -> ..._from_files
#   - phyluce_align_format_nexus_files_for_raxml       -> phyluce_align_concatenate_alignments
TEMPLATES = {
    "illumiprocessor": "illumiprocessor",
    "spades": "phyluce_assembly_assemblo_spades",
    "velvet": "phyluce_assembly_assemblo_velvet",
    "abyss": "phyluce_assembly_assemblo_abyss",
    "match_contigs_to_probes": "phyluce_assembly_match_contigs_to_probes",
    "get_match_counts": "phyluce_assembly_get_match_counts",
    "get_fastas_from_match_counts": "phyluce_assembly_get_fastas_from_match_counts",
    "explode_get_fastas_file": "phyluce_assembly_explode_get_fastas_file",
    "secap_align": "phyluce_align_seqcap_align",
    "gblocks": "phyluce_align_get_gblocks_trimmed_alignments_from_untrimmed",
    "remove_locus_name_from_files": "phyluce_align_remove_locus_name_from_files",
    "get_only_loci_with_min_taxa": "phyluce_align_get_only_loci_with_min_taxa",
    "concatenate_alignments": "phyluce_align_concatenate_alignments",
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
            # capture_output was added in Python 3.7; Phyluce 1.7 runs on 3.6,
            # so request the pipes explicitly for compatibility.
            "stdout": PIPE,
            "stderr": PIPE,
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
