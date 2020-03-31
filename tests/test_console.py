import click.testing
import pytest

from uceasy import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


@pytest.mark.e2e
def test_main_succeeds_in_production(runner):
    result = runner.invoke(console.cli)
    assert result.exit_code == 0