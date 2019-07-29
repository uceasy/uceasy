from uceasy.adapters import CPU, PHYLUCE


class UCEProcessor:


    def match_contigs_to_probes(self, output, contigs, probes):
        return [
            PHYLUCE + '/bin/phyluce_assembly_match_contigs_to_probes',
            '--contigs', contigs,
            '--probes', probes,
            '--output', output
        ]


    def get_match_counts(self, output, locus_db, taxon_list_config, taxon_group):
        return [
            PHYLUCE + '/bin/phyluce_assembly_get_match_counts',
            '--locus-db', locus_db,
            '--taxon-list-config', taxon_list_config,
            '--taxon-group', taxon_group,
            '--output', output,
            '--incomplete-matrix'
        ]


    def get_fastas_from_match_counts(self, output, contigs, locus_db, match_count_output, log):
        return [
            PHYLUCE + '/bin/phyluce_assembly_get_fastas_from_match_counts',
            '--contigs', contigs,
            '--locus-db', locus_db,
            '--match-count-output', match_count_output,
            '--output', output,
            '--log-path', log
        ]


    def explode_get_fastas_file(self, output, alignments):
        return [
            PHYLUCE + '/bin/phyluce_assembly_explode_get_fastas_file',
            '--alignments', alignments,
            '--output', output,
            '--by-taxon'
        ]

    def seqcap_align(self, output, fasta, taxa, aligner, no_trim=False):
        cmd = [
            PHYLUCE + '/bin/phyluce_align_seqcap_align',
            '--fasta', fasta,
            '--taxa', taxa,
            '--aligner', aligner,
            '--output', output,
            '--incomplete-matrix'
        ]
        if no_trim:
            cmd.append('--no-trim', '--output-format fasta')
        return cmd


    def get_gblocks_trimmed_alignments_from_untrimmed(self, output, alignments, log):
        return [
            PHYLUCE + '/bin/get_gblocks_trimmed_alignments_from_untrimmed',
            '--alignments', alignments,
            '--output', output,
            '--log', log
            ]


    def remove_locus_name_from_nexus_lines(self, output, alignments, log):
        return [
            PHYLUCE + '/bin/remove_locus_name_from_nexus_lines',
            '--alignments', alignments,
            '--output', output,
            '--log-path', log,
            '--cores', CPU
        ]


    def get_only_loci_with_min_taxa(self, output, alignments, taxa, percent, log):
        return [
            PHYLUCE + '/bin/get_only_loci_with_min_taxa',
            '--alignments', alignments,
            '--taxa', taxa,
            '--percent', percent,
            '--output', output,
            '--cores', CPU,
            '--log-path', log
        ]


    def format_nexus_files_for_raxml(self, output, alignments, log, charsets=False):
        cmd = [
            PHYLUCE + '/bin/format_nexus_files_for_raxml',
            '--alignments', alignments,
            '--output', output,
            '--log-path', log
        ]
        if charsets:
            cmd.append('--charsets')
        return cmd

