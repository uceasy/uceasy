import subprocess
from uceasy.adapters.uce_processor import UCEProcessor


class UCEPhylogenomics:


    def __init__(self, output, contigs, probes, log, taxon_group, taxa, aligner, charsets, percent, internal_trimming):
        self.__processor = UCEProcessor()
        self.__output = output
        self.__contigs = contigs
        self.__probes = probes
        self.__log = log
        self.__taxon_group = taxon_group
        self.__taxa = taxa
        self.__aligner = aligner
        self.__charsets = charsets
        self.__percent = percent
        self.__internal_trimming = internal_trimming


    def run_uce_processing(self):
        commands = []

        commands.append(self._get_match_contigs_to_probes())
        commands.append(self._get_get_match_counts())
        commands.append(self._get_get_fastas_from_match_counts())
        commands.append(self._get_explode_get_fastas_file())
        commands.append(self._get_secap_align())
        if self.__internal_trimming:
            commands.append(self._get_get_gblocks_trimmed_alignments_from_untrimmed())
            commands.append(self._get_remove_locus_name_from_nexus_lines())
            commands.append(self._get_get_only_loci_with_min_taxa())
        commands.append(self._get_nexus_files_for_raxml())

        # TODO
        # Implement subprocess call to run all these functions


        
    def _get_match_contigs_to_probes(self):
        self.__locus_db = self.__output + '/uce_search_results/probe.matches.sqlite'

        return self.__processor.match_contigs_to_probes(self.__output + '/uce_search_results',
                                                        self.__contigs,
                                                        self.__probes)
       
    
    def _get_get_match_counts(self):
        self.__alignments = self.__output + '/all_taxa_incomplete.fasta'

        return self.__processor.get_match_counts(self.__alignments,
                                                 self.__locus_db,
                                                 self.__output + '/config/taxon_set.conf',
                                                 self.__taxon_group)
   

    def _get_get_fastas_from_match_counts(self):
        return self.__processor.get_fastas_from_match_counts(self.__alignments,
                                                             self.__contigs,
                                                             self.__locus_db,
                                                             self.__output + '/config/all_taxa_incomplete.conf',
                                                             self.__log)
    

    def _get_explode_get_fastas_file(self):
        return self.__processor.explode_get_fastas_file(self.__output + '/exploded_fastas', self.__alignments)


    def _get_secap_align(self):
        self.__nexus_files = self.__output + '/nexus_files'

        return self.__processor.seqcap_align(self.__nexus_files,
                                             self.__alignments,
                                             self.__taxa,
                                             self.__aligner,
                                             self.__internal_trimming)


    def _get_get_gblocks_trimmed_alignments_from_untrimmed(self):
        cmd = self.__processor.get_gblocks_trimmed_alignments_from_untrimmed(self.__nexus_files + '_gblocks',
                                                                              self.__nexus_files,
                                                                              self.__log)

        self.__nexus_files = self.__nexus_files + '_gblocks'
        return cmd


    def _get_remove_locus_name_from_nexus_lines(self):
        cmd = self.__processor.remove_locus_name_from_nexus_lines(self.__nexus_files + '_clean',
                                                                  self.__nexus_files,
                                                                   self.__log)
        self.__nexus_files = self.__nexus_files + '_clean'
        return cmd
    

    def _get_get_only_loci_with_min_taxa(self):
        cmd = self.__processor.get_only_loci_with_min_taxa(self.__nexus_files + '_min_taxa',
                                                            self.__nexus_files,
                                                            self.__taxa,
                                                            self.__percent,
                                                            self.__log)
        self.__nexus_files = self.__nexus_files + '_min_taxa'
        return cmd


    def _get_nexus_files_for_raxml(self):
        cmd = self.__processor.format_nexus_files_for_raxml(self.__nexus_files + '_raxml',
                                                             self.__nexus_files,
                                                             self.__log,
                                                             self.__charsets)
        self.__nexus_files = self.__nexus_files = '_raxml'
        return cmd
