import pytest
import cli.uceasy_cli as cli
from click.testing import CliRunner


@pytest.fixture()
def runner():
    return CliRunner()


def test_run(runner):
    result = runner.invoke(cli.run)

    assert result.exit_code == 0
    assert result.output == 'Running all steps'


def test_web(runner):
    pass


def test_quality_control(runner):
    pass


def test_assembly(runner):
    pass


def test_uce_processing():
    pass
