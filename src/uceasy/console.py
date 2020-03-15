import click

from . import __version__


@click.group()
@click.version_option(version=__version__)
def cli():
    """A unified CLI for the PHYLUCE software package."""
    pass


@cli.command()
def quality_control():
    pass


@cli.command()
def assembly():
    pass


@cli.command()
def uce_processing():
    pass
