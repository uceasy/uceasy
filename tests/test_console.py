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


@pytest.mark.e2e
def test_quality_control(context, runner):
    params = [
        "quality-control",
        "--output",
        context["output"],
        context["raw_fastq"],
        context["csv"],
    ]
    result = runner.invoke(console.cli, params)
    assert result.exit_code == 0


@pytest.mark.e2e
def test_assembly(context, runner):
    params = [
        "assembly",
        "--output",
        context["output"],
        context["clean_fastq"],
    ]
    result = runner.invoke(console.cli, params)
    assert result.exit_code == 0
