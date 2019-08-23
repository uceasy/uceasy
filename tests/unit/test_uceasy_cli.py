import pytest
import cli.uceasy_cli as cli
from click.testing import CliRunner


ADAPTER_I5 = 'AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG'
ADAPTER_I7 = 'AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT'
SAMPLE_SHEET = 'test.csv'


@pytest.fixture()
def runner():
    return CliRunner()


def test_should_pass_when_uceasy_web_subcommand_chosen(runner):
    result = runner.invoke(cli.uceasy, ['web'])

    assert result.output == 'Web GUI\n'

