import click


@click.group()
def uceasy():
    pass


@uceasy.command()
def cmd1():
    """Command on web"""
    pass


@uceasy.command()
def cmd2():
    """Command on web"""
    pass
