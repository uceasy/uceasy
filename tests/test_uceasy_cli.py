import pytest
import cli.uceasy_cli as cli
from click.testing import CliRunner


@pytest.fixture()
def runner():
    return CliRunner()


def test_run(runner):
    pass


def test_web(runner):
    pass


def test_quality_control(runner):
    pass


def test_assembly(runner):
    pass


def test_uce_processing():
    pass
