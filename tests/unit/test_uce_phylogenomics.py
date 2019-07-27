from uceasy.uce_processors.uce_phylogenomics import UCEPhylogenomics

import pytest
import subprocess


@pytest.fixture
def processor():
    return UCEPhylogenomics('testdata/output',
                            'testdata/output/trinity/contigs',
                            'testdata/probes.fasta',
                            'testdata/output/logs')



def test_get_match_counts(processor):
    cmd = subprocess.run(processor.get_match_contigs_to_probes(), check=True) 

    assert cmd.returncode == 0
