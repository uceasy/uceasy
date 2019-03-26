import click


@click.group()
def uceasy():
    pass


@uceasy.command()
@click.option('--sheet', required=True)
@click.option('--adapter_i7', '-7', required=True)
@click.option('--adapter_i5', '-5', required=True)
@click.option('--phred33', 'fastq_encoding', flag_value='phred33',
              required=True)
@click.option('--phred64', 'fastq_encoding', flag_value='phred64')
def ctl(sheet, adapter_i7, adapter_i5, fastq_encoding):
    click.echo(f'{sheet} {adapter_i7} {adapter_i5} {fastq_encoding}')


@uceasy.command()
def web():
    click.echo('Web GUI')
