import pytest
import cli.uceasy_cli as cli
from click.testing import CliRunner
from controller.phyluce_facade import run_quality_control


ADAPTER_I5 = 'AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG'
ADAPTER_I7 = 'AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT'
SAMPLE_SHEET = 'sample/alligator_sheet.csv'
INPUT = 'sample/raw_fastq'


@pytest.fixture()
def runner():
    return CliRunner()


def test_run_illumiprocessor():
    cmd = run_quality_control(INPUT, SAMPLE_SHEET, ADAPTER_I7, ADAPTER_I5)
    assert cmd.returncode == 0
