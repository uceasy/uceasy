import pytest
import cli.uceasy_cli as cli
from click.testing import CliRunner


@pytest.fixture()
def runner():
    return CliRunner()


def test_run(runner):
    result = runner.invoke(cli.uceasy, ['run'])

    assert result.exit_code == 0
    assert result.output == 'Running all steps\n'


def test_web(runner):
    pass
