import click


@click.group()
def uceasy():
    pass


@uceasy.command()
def cmd1():
    """Command on uceasy"""
    click.echo('uceasy cmd1')


@uceasy.command()
def cmd2():
    """Command on uceasy"""
    click.echo('uceasy cmd2')


if __name__ == '__main__':
    uceasy()
