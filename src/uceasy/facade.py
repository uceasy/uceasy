from abc import ABC, abstractmethod
from typing import List
from types import SimpleNamespace
import os


from uceasy.adapters import Adapters
from uceasy.ioutils import dump_config_file, get_taxa_from_contigs, load_csv
from uceasy.operations import (
    parse_taxon_list_config,
    parse_illumiprocessor_config,
    parse_assembly_config,
)


class Facade(ABC):
    def __init__(self, context: SimpleNamespace):
        self.context: SimpleNamespace = context
        self.adapters: dict = Adapters().adapters

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError("Facade::run()")


class QualityControlFacade(Facade):
    def run(self) -> None:
        if not os.path.exists(self.context.output):
            os.makedirs(self.context.output)

        # Create and save the configuration file
        config = self.context.output + "/illumiprocessor.conf"
        csv = load_csv(self.context.csv_file)
        config_dict = parse_illumiprocessor_config(csv)
        dump_config_file(config, config_dict)

        cmd = [
            "--input",
            self.context.raw_fastq,
            "--output",
            self.context.output + "/clean_fastq",
            "--cores",
            str(self.context.threads),
            "--config",
            config,
        ]

        if self.context.min_len:
            cmd.extend(["--min-len", str(self.context.min_len)])
        if self.context.r1_pattern:
            cmd.extend(["--r1-pattern", self.context.r1_pattern])
        if self.context.r2_pattern:
            cmd.extend(["--r2-pattern", self.context.r2_pattern])
        if self.context.phred64:
            cmd.extend(["--phred", "phred64"])
        if self.context.single_end:
            cmd.append("--se")
        if self.context.no_merge:
            cmd.append("--no-merge")

        self.adapters["illumiprocessor"](cmd)


class AssemblyFacade(Facade):
    def run(self) -> None:
        if not os.path.exists(self.context.output):
            os.makedirs(self.context.output)

        # Create and save the configuration file
        if not self.context.config:
            self.context.config = self.context.output + "/assembly.conf"
            config_dict = parse_assembly_config(self.context.clean_fastq)
            dump_config_file(self.context.config, config_dict)

        cmd = [
            "--output",
            self.context.output + f"/{self.context.assembler}-assemblies",
            "--cores",
            str(self.context.threads),
            "--config",
            self.context.config,
        ]

        if self.context.assembler == "spades":
            if self.context.no_clean:
                cmd.append("--do-not-clean")
            if self.context.kmer:
                cmd.extend(["--kmer", str(self.context.kmer)])
        elif self.context.assembler == "trinity":
            if not self.context.no_clean:
                cmd.append("--clean")
            if self.context.kmer:
                cmd.extend(["--min-kmer-coverage", str(self.context.kmer)])

        if self.context.subfolder:
            cmd.extend(["--subfolder", self.context.subfolder])

        self.adapters[self.context.assembler](cmd)


class UCEPhylogenomicsFacade(Facade):
    def run(self) -> None:
        if not os.path.exists(self.context.output):
            os.makedirs(self.context.output)

        self.context.threads = str(self.context.threads)
        self.context.percent = str(self.context.percent)
        self.context.taxa = str(get_taxa_from_contigs(self.context.contigs))
        self.context.taxon_group = "all"

        self.output_dirs = {
            "match_contigs": "uce-search-results",
            "match_counts": "all-taxa.conf",
            "incomplete_matrix": "all-taxa.incomplete",
            "fasta": "all-taxa.fasta",
            "exploded_fastas": "exploded-fastas",
            "alignments": "alignments",
            "alignments_clean": "alignments-clean",
            "gblocks": "alignments-gblocks",
            "gblocks_clean": "alignments-gblocks-clean",
            "min_taxa": "alignments-gblocks-clean-min-taxa",
            "raxml": "alignments-raxml",
        }
        # Prefixing with context output
        for k, v in self.output_dirs.items():
            self.output_dirs[k] = f"{self.context.output}/{v}"

        self.context.locus_db = self.output_dirs["match_contigs"] + "/probe.matches.sqlite"

        self.context.taxon_list_config = f"{self.context.output}/taxon-list.conf"
        taxon_list_config_dict = parse_taxon_list_config(
            self.context.contigs, self.context.taxon_group
        )
        dump_config_file(self.context.taxon_list_config, taxon_list_config_dict)

        self._match_contigs_to_probes()
        self._get_match_counts()
        self._get_fastas_from_match_counts()
        self._explode_get_fastas_file()
        self._secap_align()
        if self.context.internal_trimming:
            self._get_gblocks_trimmed_alignments_from_untrimmed()
        self._remove_locus_name_from_nexus_lines()
        self._get_only_loci_with_min_taxa()
        self._nexus_files_to_raxml()

    def _match_contigs_to_probes(self) -> List[str]:
        cmd = [
            "--output",
            self.output_dirs["match_contigs"],
            "--contigs",
            self.context.contigs,
            "--probes",
            self.context.probes,
        ]
        if self.context.regex:
            cmd.extend(["--regex", self.context.regex])
        return self.adapters["match_contigs_to_probes"](cmd)

    def _get_match_counts(self) -> List[str]:
        cmd = [
            "--output",
            self.output_dirs["match_counts"],
            "--locus-db",
            self.context.locus_db,
            "--taxon-list-config",
            self.context.taxon_list_config,
            "--taxon-group",
            self.context.taxon_group,
        ]
        if self.context.incomplete_matrix:
            cmd.append("--incomplete-matrix")
        return self.adapters["get_match_counts"](cmd)

    def _get_fastas_from_match_counts(self) -> List[str]:
        cmd = [
            "--output",
            self.output_dirs["fasta"],
            "--match-count-output",
            self.output_dirs["match_counts"],
            "--contigs",
            self.context.contigs,
            "--locus-db",
            self.context.locus_db,
        ]
        if self.context.incomplete_matrix:
            cmd.append("--incomplete-matrix")
            cmd.append(self.output_dirs["incomplete_matrix"])
        return self.adapters["get_fastas_from_match_counts"](cmd)

    def _explode_get_fastas_file(self) -> List[str]:
        cmd = [
            "--input",
            self.output_dirs["fasta"],
            "--output",
            self.output_dirs["exploded_fastas"],
            "--by-taxon",
        ]
        return self.adapters["explode_get_fastas_file"](cmd)

    def _secap_align(self) -> List[str]:
        cmd = [
            "--output",
            self.output_dirs["alignments"],
            "--fasta",
            self.output_dirs["fasta"],
            "--taxa",
            self.context.taxa,
            "--aligner",
            self.context.aligner,
            "--cores",
            self.context.threads,
        ]
        if self.context.incomplete_matrix:
            cmd.append("--incomplete-matrix")
        if self.context.internal_trimming:
            cmd.extend(["--no-trim", "--output-format", "fasta"])

        return self.adapters["secap_align"](cmd)

    def _get_gblocks_trimmed_alignments_from_untrimmed(self) -> List[str]:
        """
        Run gblocks trimming on the alignments.
        The alignments must be in fasta format.
        """
        cmd = [
            "--output",
            self.output_dirs["gblocks"],
            "--alignments",
            self.output_dirs["alignments"],
            "--cores",
            self.context.threads,
        ]
        self.output_dirs["alignments"] = self.output_dirs["gblocks"]
        return self.adapters["gblocks"](cmd)

    def _remove_locus_name_from_nexus_lines(self) -> List[str]:
        cmd = [
            "--output",
            self.output_dirs["alignments_clean"],
            "--alignments",
            self.output_dirs["alignments"],
            "--cores",
            self.context.threads,
        ]
        return self.adapters["remove_locus_name_from_nexus_lines"](cmd)

    def _get_only_loci_with_min_taxa(self) -> List[str]:
        cmd = [
            "--output",
            self.output_dirs["min_taxa"],
            "--alignments",
            self.output_dirs["alignments_clean"],
            "--taxa",
            self.context.taxa,
            "--percent",
            self.context.percent,
            "--cores",
            self.context.threads,
        ]
        self.output_dirs["alignments_clean"] = self.output_dirs["min_taxa"]
        return self.adapters["get_only_loci_with_min_taxa"](cmd)

    def _nexus_files_to_raxml(self) -> List[str]:
        cmd = [
            "--output",
            self.output_dirs["raxml"],
            "--alignments",
            self.output_dirs["min_taxa"],
        ]

        if self.context.charsets:
            cmd.append("--charsets")
        return self.adapters["nexus_to_raxml"](cmd)
