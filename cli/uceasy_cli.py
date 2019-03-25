import click


@click.group(invoke_without_command=True)
@click.argument('config')
@click.pass_context
def uceasy(ctx, config):
    if ctx.invoked_subcommand is None:
        click.echo('Web GUI')
    else:
        click.echo(config)
