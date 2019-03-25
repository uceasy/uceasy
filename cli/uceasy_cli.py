import click


@click.group()
def uceasy():
    pass


@uceasy.command()
def run():
    click.echo('Running all steps')


@uceasy.command()
def web():
    pass
