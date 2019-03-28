import click


@click.group()
def uceasy():
    pass


@uceasy.command()
@click.option('--sheet', required=True)
@click.option('--adapter_i7', '-i7', required=True)
@click.option('--adapter_i5', '-i5', required=True)
@click.option('--phred33', 'fastq_encoding', flag_value='phred33', required=True)
@click.option('--phred64', 'fastq_encoding', flag_value='phred64')
@click.option('--min_len', type=int)
@click.option('--r1_pattern', '-r1')
@click.option('--r2_pattern', '-r2')
@click.option('--no_merge', flag_value='no_merge')
@click.option('--single-end', flag_value='single_end')
def ctl(sheet, adapter_i7, adapter_i5, fastq_encoding, min_len, r1_pattern, r2_pattern,
        no_merge, single_end):

    click.echo(f'{sheet} {adapter_i7} {adapter_i5} {fastq_encoding} {min_len}' +
               f'{r1_pattern} {r2_pattern} {no_merge} {single_end}')


@uceasy.command()
def web():
    click.echo('Web GUI')
