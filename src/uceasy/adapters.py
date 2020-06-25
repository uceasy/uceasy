r"""Adapters is a dictionary to call command-line programs.

Specify the program with the dictionary key and its arguments as a list.
e.g. adapters["program"](["arg1", "arg2"])
"""


from subprocess import run
from typing import List, Dict, Optional, Any


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

    def add(self, name: str, binary: str) -> None:
        """Add new adapter to the dictionary."""

        def func(
            args_as_list: List[str], capture_output: bool = False, dir_to_execute: str = None
        ) -> List[str]:
            """Provide the adapter arguments as a list via "args_as_list"."""
            cmd = [binary] + args_as_list
            return self._run(cmd, capture_output, dir_to_execute)

        self.adapters[name] = func

    def _run(
        self, cmd: List[str], capture_output: bool, dir_to_execute: Optional[str]
    ) -> List[str]:
        """
        Utilitary runner to be used by the adapters.

        :param cmd              the command passed by the adapter as a list.
        :param capture_output   True if you want to receive the output of the
                                command.
        :param dir_to_execute   execute in a different directory.
        :return:                empty list in case of "capture_output=False",
                                otherwise the lines of the command output as a
                                list. One line of output is one item in the
                                list.
        """
        kwargs: Dict[str, Any] = {
            "cwd": dir_to_execute,
            "capture_output": capture_output,
            "universal_newlines": capture_output,  # receive as string not bytes
        }
        cmd_return = run(cmd, **kwargs)

        return cmd_return.stdout.strip().splitlines() if capture_output else []
