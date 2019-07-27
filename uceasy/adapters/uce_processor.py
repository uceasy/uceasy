import subprocess
import abc
from uceasy.adapters import CPU, PHYLUCE


class UCEProcessor(metaclass=abc.ABCMeta):


    def __init__(self, output, contigs, log):
        self.__output = output
        self.__contigs = contigs
        self.__log = log


    @abc.abstractmethod
    def run_uce_processing(self):
        pass


    def match_contigs_to_probes(self, probes):
        return [
            PHYLUCE + '/bin/phyluce_assembly_match_contigs_to_probes',
            '--contigs', self.__contigs,
            '--probes', probes,
            '--output', self.__output
        ]


    def get_match_counts(self, locus_db, taxon_list_config, taxon_group):
        return [
            PHYLUCE + '/bin/phyluce_assembly_get_match_counts',
            '--locus-db', locus_db,
            '--taxon-list-config', taxon_list_config,
            '--taxon-group', taxon_group,
            '--output', self.__output
        ]


    def get_fastas_from_match_counts(self, locus_db, match_count_output):
        return [
            PHYLUCE + '/bin/phyluce_assembly_get_fastas_from_match_counts',
            '--contigs', self.__contigs,
            '--locus-db', locus_db,
            '--match-count-output', match_count_output,
            '--output', self.__output,
            '--log-path', self.__log
        ]


    def explode_get_fastas_file(self, alignments):
        return [
            PHYLUCE + '/bin/phyluce_assembly_explode_get_fastas_file',
            '--alignments', alignments,
            '--output', self.__output,
            '--by-taxon'
        ]

    def seqcap_align(self, fasta, taxa, aligner, no_trim=False):
        cmd = [
            PHYLUCE + '/bin/phyluce_align_seqcap_align',
            '--fasta', fasta,
            '--taxa', taxa,
            '--aligner', aligner,
            '--output', self.__output
        ]
        if no_trim:
            cmd.append('--no-trim')
        return cmd


    def get_gblocks_trimmed_alignments_from_untrimmed(self, alignments):
        return [
            PHYLUCE + '/bin/get_gblocks_trimmed_alignments_from_untrimmed',
            '--alignments', alignments,
            '--output', self.__output,
            '--log', self.__log
            ]


    def remove_locus_name_from_nexus_lines(self, alignments):
        return [
            PHYLUCE + '/bin/remove_locus_name_from_nexus_lines',
            '--alignments', alignments,
            '--output', self.__output,
            '--log-path', self.__log,
            '--cores', CPU
        ]


    def get_only_loci_with_min_taxa(self, alignments, taxa, percent):
        return [
            PHYLUCE + '/bin/get_only_loci_with_min_taxa',
            '--alignments', alignments,
            '--taxa', taxa,
            '--percent', percent,
            '--output', self.__output,
            '--cores', CPU,
            '--log-path', self.__log
        ]


    def format_nexus_files_for_raxml(self, alignments, charsets=False):
        cmd = [
            PHYLUCE + '/bin/format_nexus_files_for_raxml',
            '--alignments', alignments,
            '--output', self.__output,
            '--log-path', self.__log
        ]
        if charsets:
            cmd.append('--charsets')
        return cmd

