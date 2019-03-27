import pytest
import facade.trinity as trinity


CLEAN_FASTQ = '../../workenv/data/clean_fastq'
SAMPLE_NAMES = 'alligator_mississippiensis'


def test_prepare_samples_for_conf_file():
    samples = trinity.prepare_samples_for_conf_file([SAMPLE_NAMES], CLEAN_FASTQ)

    assert samples[0] == f'{SAMPLE_NAMES}:{CLEAN_FASTQ}/{SAMPLE_NAMES}/split-adapter-quality-trimmed/'


def test_run_assembly():
    pass
