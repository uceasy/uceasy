from uceasy.use_cases.uce_phylogenomics import UCEPhylogenomics

import pytest
import subprocess


@pytest.fixture
def processor():
    return UCEPhylogenomics('testoutput',
                            'testdata/contigs',
                            'testdata/probes.fasta',
                            'testoutput/logs',
                            'all',
                            1,
                            'mafft',
                            True,
                            0.75,
                            False)



def test_get_match_counts(processor):
    cmd = processor.run_uce_processing()

    assert cmd.returncode == 0
