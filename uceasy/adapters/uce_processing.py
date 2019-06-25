import subprocess
from adapters import CPU, PHYLUCE


def match_contigs_to_probes(contigs, probes, output):
    cmd = [
        PHYLUCE + '/bin/phyluce_assembly_match_contigs_to_probes',
        '--contigs', contigs,
        '--probes', probes,
        '--output', output 
    ]
    return subprocess.run(cmd, check=True)


def get_match_counts(locus_db, taxon_list_config, taxon_group, output):
    cmd = [
        PHYLUCE + '/bin/phyluce_assembly_get_match_counts',
        '--locus-db', locus_db,
        '--taxon-list-config', taxon_list_config,
        '--taxon-group', taxon_group,
        '--output', output 
    ]
    return subprocess.run(cmd, check=True)


def get_fastas_from_match_counts(contigs, locus_db, match_count_output, output, log_path):
    cmd = [
        PHYLUCE + '/bin/phyluce_assembly_get_fastas_from_match_counts',
        '--contigs', contigs,
        '--locus-db', locus_db,
        '--match-count-output', match_count_output,
        '--output', output,
        '--log-path', log_path
    ]
    return subprocess.run(cmd, check=True)


def explode_get_fastas_file(alignments, output):
    cmd = [
        PHYLUCE + '/bin/phyluce_assembly_explode_get_fastas_file',
        '--alignments', alignments,
        '--output', output,
        '--by-taxon'
    ]
    return subprocess.run(cmd, check=True)


def seqcap_align(fasta, taxa, aligner, output, no_trim=False):
    cmd = [
        PHYLUCE + '/bin/phyluce_align_seqcap_align',
        '--fasta', fasta,
        '--taxa', taxa,
        '--aligner', aligner,
        '--output', output
    ]
    if no_trim:
        cmd.append('--no-trim')
    return subprocess.run(cmd, check=True)


def get_gblocks_trimmed_alignments_from_untrimmed(alignments, output, log):
    cmd = [
        PHYLUCE + '/bin/get_gblocks_trimmed_alignments_from_untrimmed',
        '--alignments', alignments,
        '--output', output,
        '--log', log
        ]
    return subprocess.run(cmd, check=True)


def remove_locus_name_from_nexus_lines(alignments, output, log):
    cmd = [
        PHYLUCE + '/bin/remove_locus_name_from_nexus_lines',
        '--alignments', alignments,
        '--output', output,
        '--log-path', log,
        '--cores', CPU
    ]
    return subprocess.run(cmd, check=True)


def get_only_loci_with_min_taxa(alignments, taxa, percent, output, log):
    cmd = [
        PHYLUCE + '/bin/get_only_loci_with_min_taxa',
        '--alignments', alignments,
        '--taxa', taxa,
        '--percent', percent,
        '--output', output,
        '--cores', CPU,
        '--log-path', log
    ]
    return subprocess.run(cmd, check=True)


def format_nexus_files_for_raxml(alignments, output, log, charsets=False):
    cmd = [
        PHYLUCE + '/bin/format_nexus_files_for_raxml',
        '--alignments', alignments,
        '--output', output,
        '--log-path', log
    ]
    if charsets:
        cmd.append('--charsets')
    return subprocess.run(cmd, check=True)

