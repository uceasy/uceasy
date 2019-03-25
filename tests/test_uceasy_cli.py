import pytest
import cli.uceasy_cli as cli
from click.testing import CliRunner


@pytest.fixture()
def runner():
    return CliRunner()


def test_should_pass_when_uceasy_web_subcommand_chosen(runner):
    result = runner.invoke(cli.uceasy, ['web'])

    assert result.output == 'Web GUI\n'


def test_should_pass_when_ctl_phred33_chosen(runner):
    result = runner.invoke(cli.uceasy, ['ctl', '--phred33'])

    assert result.output == 'Phred33\n'
