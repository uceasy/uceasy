import subprocess
from uceasy.adapters.uce_processor import UCEProcessor


class UCEPhylogenomics:


    def __init__(self, output, contigs, probes, log):
        self.__processor = UCEProcessor()
        self.__output = output
        self.__contigs = contigs
        self.__probes = probes
        self.__log = log


    def run_uce_processing(self):
        commands = []

        commands.append(self.get_match_contigs_to_probes())


        
    def get_match_contigs_to_probes(self):
        self.__locus_db = self.__output + '/uce_search_results/probe.matches.sqlite'

        return self.__processor.match_contigs_to_probes(self.__output + '/uce_search_results',
                                                        self.__contigs,
                                                        self.__probes)
       
    
    def get_get_match_counts(self):
        pass

