import pytest
import cli.uceasy_cli as cli
from click.testing import CliRunner


@pytest.fixture()
def runner():
    return CliRunner()


def test_run(runner):
    result = runner.invoke(cli.uceasy, ['flag'])

    assert result.exit_code == 0
    assert result.output == 'flag\n'


def test_run(runner):
    result = runner.invoke(cli.uceasy, [''])

    assert result.exit_code == 0
    assert result.output == 'Web GUI\n'
