import pytest
import cli.uceasy_cli as cli
from click.testing import CliRunner


@pytest.fixture()
def runner():
    return CliRunner()


def test_uceasy(runner):
    result = runner.invoke(cli.uceasy, ['flag'])

    assert result.exit_code == 0
    assert result.output == 'flag\n'


def test_should_pass_when_uceasy_run_without_flags(runner):
    result = runner.invoke(cli.uceasy, [''])

    assert result.exit_code == 0
    assert result.output == 'Web GUI\n'
