from typing import List, Optional
import os


from .adapters import Adapters
from .ioutils import dump_config_file, get_taxa_from_contigs, load_csv
from .operations import (
    parse_taxon_list_config,
    parse_illumiprocessor_config,
    parse_assembly_config,
)


class QualityControlFacade:
    def __init__(
        self,
        raw_fastq: str,
        csv_file: str,
        threads: int,
        single_end: bool,
        single_index: bool,
        r1_pattern: Optional[str],
        r2_pattern: Optional[str],
        phred64: bool,
        output: str,
        min_len: Optional[int],
        no_merge: bool,
    ):
        self._raw_fastq = raw_fastq
        self._csv_file = csv_file
        self._threads = str(threads)
        self._single_end = single_end
        self._single_index = single_index
        self._r1_pattern = r1_pattern
        self._r2_pattern = r2_pattern
        self._phred64 = phred64
        self._output = output
        self._min_len = str(min_len)
        self._no_merge = no_merge
        self._config = output + "/illumiprocessor.conf"
        self._adapters = Adapters().adapters

        if not os.path.exists(output):
            os.makedirs(output)

    def run(self) -> None:
        # Create and save the configuration file
        csv = load_csv(self._csv_file)
        config_dict = parse_illumiprocessor_config(csv)
        dump_config_file(self._config, config_dict)

        cmd = [
            "--input",
            self._raw_fastq,
            "--output",
            self._output + "/clean_fastq",
            "--cores",
            self._threads,
            "--config",
            self._config,
        ]

        if self._min_len:
            cmd.extend(["--min-len", self._min_len])
        if self._r1_pattern:
            cmd.extend(["--r1-pattern", self._r1_pattern])
        if self._r2_pattern:
            cmd.extend(["--r2-pattern", self._r2_pattern])
        if self._phred64:
            cmd.extend(["--phred", "phred64"])
        if self._single_end:
            cmd.append("--se")
        if self._no_merge:
            cmd.append("--no-merge")

        self._adapters["illumiprocessor"](cmd)


class AssemblyFacade:
    def __init__(
        self,
        clean_fastq: str,
        threads: int,
        output: str,
        config: Optional[str],
        kmer: Optional[str],
        no_clean: bool,
        subfolder: Optional[str],
    ):
        self._clean_fastq = clean_fastq
        self._threads = str(threads)
        self._output = output
        self._config = config
        self._kmer = kmer
        self._no_clean = no_clean
        self._subfolder = subfolder
        self._adapters = Adapters().adapters

        if not os.path.exists(output):
            os.makedirs(output)

    def run(self) -> None:
        # Create and save the configuration file
        if not self._config:
            self._config = self._output + "/assembly.conf"
            config_dict = parse_assembly_config(self._clean_fastq)
            dump_config_file(self._config, config_dict)

        cmd = [
            "--output",
            self._output + "/spades-assemblies",
            "--cores",
            self._threads,
            "--config",
            self._config,
        ]

        if self._no_clean:
            cmd.append("--do-not-clean")
        if self._kmer:
            cmd.extend(["--kmer", self._kmer])
        if self._subfolder:
            cmd.extend(["--subfolder", self._subfolder])

        self._adapters["spades"](cmd)


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
        regex: Optional[str],
    ):
        self._aligner = aligner
        self._charsets = charsets
        self._contigs = contigs
        self._internal_trimming = internal_trimming
        self._log_dir = log_dir
        self._probes = probes
        self._percent = str(percent)
        self._threads = str(threads)
        self._regex = regex
        self._adapters = Adapters().adapters
        self._taxa = str(get_taxa_from_contigs(self._contigs))
        self._taxon_list_config = f"{output_dir}/taxon-list.conf"
        self._taxon_group = "all"
        self._output_dirs = {
            "match_contigs": "uce-search-results",
            "match_counts": "all-taxa-incomplete.conf",
            "incomplete_matrix": "all-taxa-incomplete.incomplete",
            "fasta": "all-taxa-incomplete.fasta",
            "exploded_fastas": "exploded-fastas",
            "alignments": "alignments",
            "alignments_clean": "alignments-clean",
            "gblocks": "alignments-gblocks",
            "gblocks_clean": "alignments-gblocks-clean",
            "min_taxa": "alignments-gblocks-clean-min-taxa",
            "raxml": "alignments-raxml",
        }
        # Prefixing with output_dir
        for k, v in self._output_dirs.items():
            self._output_dirs[k] = f"{output_dir}/{v}"

        self._locus_db = (
            self._output_dirs["match_contigs"] + "/probe.matches.sqlite"
        )

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def run(self) -> None:
        # TODO incomplete matrix might be a cli argument

        taxon_list_config_dict = parse_taxon_list_config(
            self._contigs, self._taxon_group,
        )
        dump_config_file(
            self._taxon_list_config, taxon_list_config_dict,
        )

        self._match_contigs_to_probes()
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
            self._output_dirs["match_contigs"],
            "--contigs",
            self._contigs,
            "--probes",
            self._probes,
        ]
        if self._regex:
            cmd.extend(["--regex", self._regex])
        return self._adapters["match_contigs_to_probes"](cmd)

    def _get_match_counts(self) -> List[str]:
        cmd = [
            "--output",
            self._output_dirs["match_counts"],
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
            self._output_dirs["fasta"],
            "--match-count-output",
            self._output_dirs["match_counts"],
            "--contigs",
            self._contigs,
            "--locus-db",
            self._locus_db,
            "--incomplete-matrix",
            self._output_dirs["incomplete_matrix"],
        ]

        return self._adapters["get_fastas_from_match_counts"](cmd)

    def _explode_get_fastas_file(self) -> List[str]:
        cmd = [
            "--input",
            self._output_dirs["fasta"],
            "--output",
            self._output_dirs["exploded_fastas"],
            "--by-taxon",
        ]
        return self._adapters["explode_get_fastas_file"](cmd)

    def _secap_align(self) -> List[str]:
        cmd = [
            "--output",
            self._output_dirs["alignments"],
            "--fasta",
            self._output_dirs["fasta"],
            "--taxa",
            self._taxa,
            "--aligner",
            self._aligner,
            "--cores",
            self._threads,
        ]
        if self._internal_trimming:
            cmd.append("--no-trim")

        return self._adapters["secap_align"](cmd)

    def _get_gblocks_trimmed_alignments_from_untrimmed(self) -> List[str]:
        """Run gblocks trimming on the alignments"""
        cmd = [
            "--output",
            self._output_dirs["gblocks"],
            "--alignments",
            self._output_dirs["alignments"],
            "--cores",
            self._threads,
        ]
        self._output_dirs["alignments"] = self._output_dirs["gblocks"]
        return self._adapters["gblocks"](cmd)

    def _remove_locus_name_from_nexus_lines(self) -> List[str]:
        cmd = [
            "--output",
            self._output_dirs["alignments_clean"],
            "--alignments",
            self._output_dirs["alignments"],
            "--cores",
            self._threads,
        ]
        return self._adapters["remove_locus_name_from_nexus_lines"](cmd)

    def _get_only_loci_with_min_taxa(self) -> List[str]:
        cmd = [
            "--output",
            self._output_dirs["min_taxa"],
            "--alignments",
            self._output_dirs["alignments_clean"],
            "--taxa",
            self._taxa,
            "--percent",
            self._percent,
            "--cores",
            self._threads,
        ]
        self._output_dirs["alignments_clean"] = self._output_dirs["min_taxa"]
        return self._adapters["get_only_loci_with_min_taxa"](cmd)

    def _nexus_files_for_raxml(self) -> List[str]:
        cmd = [
            "--output",
            self._output_dirs["raxml"],
            "--alignments",
            self._output_dirs["min_taxa"],
        ]

        if self._charsets:
            cmd.append("--charsets")
        return self._adapters["nexus_to_raxml"](cmd)
