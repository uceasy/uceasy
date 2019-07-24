from uceasy.adapters import quality_control
from uceasy.controller import env_manager
import os



def test_run_illumiprocessor():
    input = 'testdata/raw_fastq'
    output = 'testdata/output/clean_fastq'
    config = 'testdata/illumiprocessor.conf'

    cmd = quality_control.run_illumiprocessor(input, output, config)

    assert cmd.returncode == 0

