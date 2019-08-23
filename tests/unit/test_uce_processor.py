import pytest
import subprocess

from uceasy.adapters.uce_processor import UCEProcessor


DATA = 'testdata'
OUTPUT = 'testoutput'
CONTIGS = 'testoutput/spades/contigs'
PROBES = 'testdata/probes.fasta'
LOCUS_DB = 'testoutput/uce-search-results/probe.matches.sqlite'
LOGS = OUTPUT
ALIGNER = 'mafft'
TAXA = '1'
PERCENT = '0.75'


@pytest.fixture
def processor():
    return UCEProcessor()


def test_get_match_contigs_to_probes(processor):
    output = OUTPUT + '/uce-search-results'

    cmd = processor.match_contigs_to_probes(output, CONTIGS, PROBES)
    assert cmd.returncode == 0


def test_get_match_counts(processor):
    config = DATA + '/taxon-set.conf'
    taxon_group = 'all'
    output = OUTPUT + '/all-taxa-incomplete.conf'
    
    cmd = processor.get_match_counts(output, LOCUS_DB, config, taxon_group)
    assert cmd.returncode == 0


def test_get_fastas_from_match_counts(processor):
    match_count_output = OUTPUT + '/all-taxa-incomplete.conf'
    incomplete_matrix = OUTPUT + '/all-taxa-incomplete.incomplete'
    output = OUTPUT + '/all-taxa-incomplete.fasta'

    cmd = processor.get_fastas_from_match_counts(output, CONTIGS, LOCUS_DB, match_count_output, incomplete_matrix, LOGS)
    assert cmd.returncode == 0


def test_explode_get_fastas_file(processor):
    input = OUTPUT + '/all-taxa-incomplete.fasta'
    output = OUTPUT + '/exploded-fastas'

    cmd = processor.explode_get_fastas_file(input, output)
    assert cmd.returncode == 0


def test_seqcap_align_edge_trimming(processor):
    fasta = OUTPUT + '/all-taxa-incomplete.fasta'
    output = OUTPUT + '/mafft-nexus-edge-trimmed'
    
    # It kept running indefinitely
    # cmd = processor.seqcap_align(output, fasta, TAXA, ALIGNER)

    assert False


def test_seqcap_align_internal_trimming(processor):
    fasta = OUTPUT + '/all-taxa-incomplete.fasta'
    output = OUTPUT + '/mafft-nexus-internal-trimmed'
    
    cmd = processor.seqcap_align(output, fasta, TAXA, ALIGNER, no_trim=True)
    assert cmd.returncode == 0


def test_get_gblocks_trimmed_alignments_from_untrimmed(processor):
    alignments = OUTPUT + '/mafft-nexus-internal-trimming'
    output = OUTPUT + '/mafft-nexus-internal-trimming-gblocks'

    cmd = processor.get_gblocks_trimmed_alignments_from_untrimmed(alignments, output, LOGS)
    assert cmd.returncode == 0



def test_remove_locus_name_from_nexus_lines(processor):
    alignments = OUTPUT +'/mafft-nexus-internal-trimming-gblocks'
    output = OUTPUT + '/mafft-nexus-internal-trimming-gblocks-clean'

    cmd = processor.remove_locus_name_from_nexus_lines(alignments, output, LOGS)
    assert cmd.returncode == 0
    

def test_get_only_loci_with_min_taxa(processor):
    alignments = OUTPUT + '/mafft-nexus-internal-trimming-gblocks-clean'
    output = OUTPUT + '/mafft-nexus-internal-trimming-gblocks-clean-min'

    cmd = processor.get_only_loci_with_min_taxa(alignments, output, TAXA, PERCENT, LOGS)
    assert cmd.returncode == 0


def test_format_nexus_files_for_raxml(processor):
    alignments = OUTPUT + '/mafft-nexus-internal-trimming-gblocks-clean-min'
    output = OUTPUT + '/mafft-nexus-internal-trimming-gblocks-clean-min-raxml'

    cmd = processor.format_nexus_files_for_raxml(alignments, output, LOGS, charsets=True)
    assert cmd.returncode == 0


