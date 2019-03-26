import pytest
import cli.uceasy_cli as cli
from click.testing import CliRunner


adapter_i5 = 'AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG'
adapter_i7 = 'AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT'
sample_sheet = 'test.csv'


@pytest.fixture()
def runner():
    return CliRunner()


def test_should_pass_when_uceasy_web_subcommand_chosen(runner):
    result = runner.invoke(cli.uceasy, ['web'])

    assert result.output == 'Web GUI\n'


def test_should_pass_when_ctl_basic_test(runner):
    result = runner.invoke(cli.uceasy, f'ctl --sheet {sample_sheet} ' +
                                       f'--adapter_i7 {adapter_i7} ' +
                                       f'--adapter_i5 {adapter_i5} ' +
                                       f'--phred33 ')

    assert f'{sample_sheet} {adapter_i7} {adapter_i5}' in result.output


def test_should_pass_when_ctl_no_merge_chosen(runner):
    result = runner.invoke(cli.uceasy, f'ctl --sheet {sample_sheet} ' +
                                       f'--adapter_i7 {adapter_i7} ' +
                                       f'--adapter_i5 {adapter_i5} ' +
                                       f'--phred33 ' +
                                       f'--no-merge')

    assert 'no_merge' in result.output


def test_should_pass_when_ctl_phred33_chosen(runner):
    result = runner.invoke(cli.uceasy, f'ctl --sheet {sample_sheet} ' +
                                       f'--adapter_i7 {adapter_i7} ' +
                                       f'--adapter_i5 {adapter_i5} ' +
                                       f'--phred33')

    assert 'phred33' in result.output


def test_should_pass_when_ctl_phred64_chosen(runner):
    result = runner.invoke(cli.uceasy, f'ctl --sheet {sample_sheet} ' +
                                       f'--adapter_i7 {adapter_i7} ' +
                                       f'--adapter_i5 {adapter_i5} ' +
                                       f'--phred64')

    assert 'phred64' in result.output
