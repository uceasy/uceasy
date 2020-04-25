from typing import List
import os


from .adapters import Adapters
from .ioutils import dump_config_file, get_taxa_from_contigs
from .operations import parse_taxon_list_config


class UCEPhylogenomicsFacade:
    def __init__(
        self,
        aligner: str,
        charsets: bool,
        contigs: str,
        internal_trimming: bool,
        output_dir: str,
        log_dir: str,
        probes: str,
        percent: float,
        threads: int,
    ):
        # From CLI
        self._aligner = aligner
        self._charsets = charsets
        self._contigs = contigs
        self._internal_trimming = internal_trimming
        self._log_dir = log_dir
        self._probes = probes
        self._percent = str(percent)
        self._threads = str(threads)

        self._taxa: str = str(get_taxa_from_contigs(contigs))
        self._adapters: dict = Adapters().adapters
        self._taxon_list_config: str = f"{output_dir}/taxon-set.conf"
        self._taxon_group: str = "all"
        self._nexus_output_format = "fasta"
        self._output: dict = {
            "match_contigs": "uce-search-results",
            "match_count": "all-taxa-incomplete.conf",
            "incomplete_matrix": "all-taxa-incomplete.incomplete",
            "fasta": "all-taxa-incomplete.fasta",
            "exploded_fastas": "exploded-fastas",
            "alignments": "aligments",
            "gblocks": "aligments-gblocks",
            "gblocks_clean": "aligments-gblocks-clean",
            "min_taxa": "aligments-gblocks-clean-min-taxa",
            "raxml": "aligments-raxml",
        }
        # Prefixing with output given by CLI
        for k, v in self._output.items():
            self._output[k] = f"{output_dir}/{v}"

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def run(self) -> None:
        # TODO incomplete matrix might be a cli argument
        self._match_contigs_to_probes()
        # Create taxon-set.conf
        taxon_list_config_string = parse_taxon_list_config(
            self._contigs, self._taxon_group,
        )
        dump_config_file(
            self._taxon_list_config,
            taxon_list_config_string,
            allow_no_value=True,
        )
        self._locus_db = self._output["match_contigs"] + "/probe.matches.sqlite"
        self._get_match_counts()
        self._get_fastas_from_match_counts()
        self._explode_get_fastas_file()
        self._secap_align()
        if self._internal_trimming:
            self._get_gblocks_trimmed_alignments_from_untrimmed()
            self._remove_locus_name_from_nexus_lines()
            self._get_only_loci_with_min_taxa()
        self._nexus_files_for_raxml()

    def _match_contigs_to_probes(self) -> List[str]:
        cmd = [
            "--output",
            self._output["match_contigs"],
            "--contigs",
            self._contigs,
            "--probes",
            self._probes,
        ]
        return self._adapters["match_contigs_to_probes"](cmd)

    def _get_match_counts(self) -> List[str]:
        cmd = [
            "--output",
            self._output["match_count"],
            "--locus-db",
            self._locus_db,
            "--taxon-list-config",
            self._taxon_list_config,
            "--taxon-group",
            self._taxon_group,
        ]
        return self._adapters["get_match_counts"](cmd)

    def _get_fastas_from_match_counts(self) -> List[str]:
        cmd = [
            "--output",
            self._output["fasta"],
            "--match-count-output",
            self._output["match_count"],
            "--contigs",
            self._contigs,
            "--locus-db",
            self._locus_db,
            "--incomplete-matrix",
            self._output["incomplete_matrix"],
        ]

        return self._adapters["get_fastas_from_match_counts"](cmd)

    def _explode_get_fastas_file(self) -> List[str]:
        cmd = [
            "--input",
            self._output["fasta"],
            "--output",
            self._output["exploded_fastas"],
            "--by-taxon",
        ]
        return self._adapters["explode_get_fastas_file"](cmd)

    def _secap_align(self) -> List[str]:
        cmd = [
            "--output",
            self._output["alignments"],
            "--fasta",
            self._output["fasta"],
            "--taxa",
            self._taxa,
            "--aligner",
            self._aligner,
            "--cores",
            self._threads,
            "--output-format",
            self._nexus_output_format,
        ]
        if self._internal_trimming:
            cmd.append("--no-trim")

        return self._adapters["secap_align"](cmd)

    def _get_gblocks_trimmed_alignments_from_untrimmed(self) -> List[str]:
        """Run gblocks trimming on the alignments"""
        cmd = [
            "--alignments",
            self._output["alignments"],
            "--output",
            self._output["gblocks"],
            "--cores",
            self._threads,
        ]
        return self._adapters["gblocks"](cmd)

    def _remove_locus_name_from_nexus_lines(self) -> List[str]:
        cmd = [
            "--alignments",
            self._output["gblocks"],
            "--output",
            self._output["gblocks_clean"],
            "--cores",
            self._threads,
        ]
        return self._adapters["remove_locus_name_from_nexus_lines"](cmd)

    def _get_only_loci_with_min_taxa(self) -> List[str]:
        cmd = [
            "--output",
            self._output["min_taxa"],
            "--alignments",
            self._output["gblocks_clean"],
            "--taxa",
            self._taxa,
            "--percent",
            self._percent,
            "--cores",
            self._threads,
        ]
        return self._adapters["get_only_loci_with_min_taxa"](cmd)

    def _nexus_files_for_raxml(self) -> List[str]:
        cmd = [
            "--output",
            self._output["raxml"],
        ]
        if self._internal_trimming:
            cmd.extend(["--alignments", self._output["min_taxa"]])
        else:
            cmd.extend(["--alignments", self._output["alignments"]])

        if self._charsets:
            cmd.append("--charsets")
        return self._adapters["nexus_to_raxml"](cmd)
