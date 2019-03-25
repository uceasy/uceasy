import click


@click.group()
def uceasy():
    pass


@uceasy.command()
@click.option('--phred33/--no-phred33', required=True)
def ctl(phred33):
    if phred33:
        click.echo('Phred33')
    else:
        click.echo('Phred64')


@uceasy.command()
def web():
    click.echo('Web GUI')
