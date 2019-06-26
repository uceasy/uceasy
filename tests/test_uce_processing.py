import subprocess
from uceasy.adapters import uce_processing


CONTIGS = './sample/test_assemblies/contigs'
PROBES = './sample/uce-5k-probes.fasta'


def test_match_contigs_to_probes():
    cmd = uce_processing.match_contigs_to_probes(CONTIGS, PROBES, './sample/uce_search_results')
    assert cmd.returncode == 0
