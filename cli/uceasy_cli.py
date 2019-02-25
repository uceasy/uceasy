import click


@click.group()
def uceasy():
    pass


@uceasy.command()
def run():
    click.echo('Running all steps')


@uceasy.command()
def quality_control():
    pass


@uceasy.command()
def assembly():
    pass


@uceasy.command()
def uce_processing():
    pass


@uceasy.command()
def web():
    pass
