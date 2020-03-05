import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """A unified CLI for the PHYLUCE software package."""
    click.echo("Hello, world!")
