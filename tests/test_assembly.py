from facade.trinity import prepare_samples_for_conf_file, run_trinity
from facade import WORKENV


CLEAN_FASTQ = '../../workenv/data/clean-fastq'
SAMPLE_NAMES = 'alligator_mississippiensis'
OUTPUT = WORKENV + 'data/trinity-assemblies'


def test_prepare_samples_for_conf_file():
    samples = prepare_samples_for_conf_file([SAMPLE_NAMES], CLEAN_FASTQ)

    assert samples[0] == f'{SAMPLE_NAMES}:{CLEAN_FASTQ}/{SAMPLE_NAMES}/split-adapter-quality-trimmed/'


def test_run_assembly():
    completed_process = run_trinity([SAMPLE_NAMES], CLEAN_FASTQ, OUTPUT)

    assert completed_process.returncode == 0
