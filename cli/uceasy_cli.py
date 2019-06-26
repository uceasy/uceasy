import click
from uceasy.controller.phyluce_facade import run_quality_control, run_assembly


@click.group()
def uceasy():
    pass


@uceasy.command()
@click.option('--input', required=True)
@click.option('--sheet', required=True)
@click.option('--adapter_i7', '-i7', required=True)
@click.option('--adapter_i5', '-i5', required=True)
@click.option('--phred33', 'fastq_encoding', flag_value='phred33', default='phred33')
@click.option('--phred64', 'fastq_encoding', flag_value='phred64')
@click.option('--min_len', type=int)
@click.option('--r1_pattern', '-r1')
@click.option('--r2_pattern', '-r2')
@click.option('--no_merge', flag_value=True, default=False)
@click.option('--single-end', flag_value=True, default=False)
def ctl(input, sheet, adapter_i7, adapter_i5, fastq_encoding, min_len, r1_pattern, r2_pattern, no_merge, single_end):
    try:
        click.echo(
            f'''
            {" Illumiprocessor parameters ":=^60}\n
            Input: {input}\n
            Sheet: {sheet}\n
            Adapter i7: {adapter_i7}\n
            Adapter i5: {adapter_i5}\n
            Encoding: {fastq_encoding}\n
            Minimum Length: {min_len}\n
            R1 Pattern: {r1_pattern}\n
            R2 Pattern: {r2_pattern}\n
            No Merge: {no_merge}\n
            Single End: {single_end}\n
            {" Assembler ":=^60}\n
            Trinity
            '''
        )
        run_quality_control(input, sheet, adapter_i7, adapter_i5)
        click.echo(f'Preprando para executar Trinity...')
        run_assembly()
    except Exception as e:
        click.echo(e)


@click.command()
def quality_control():
    click.echo('Run only quality control')


@click.command()
def assembly():
    click.echo('Run only assembly')


@uceasy.command()
def web():
    click.echo('Web GUI')
