import click


@click.group()
def uceasy():
    pass


@uceasy.command()
def run():
    """Command on web"""
    pass


@uceasy.command()
def quality_control():
    """Command on web"""
    pass


@uceasy.command()
def assembly():
    """Command on web"""
    pass


@uceasy.command()
def uce_processing():
    """Command on web"""
    pass


@uceasy.command()
def web():
    """Command on web"""
    pass
