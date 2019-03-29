from phyluce_facade.assembly import run_trinity
from phyluce_facade import CLEAN_FASTQ, WORKENV

OUTPUT = WORKENV + 'data/trinity_assemblies'


def test_run_assembly():
    samples_names = 'alligator_mississippiensis'
    completed_process = run_trinity([samples_names], CLEAN_FASTQ, OUTPUT)

    assert completed_process.returncode == 0
