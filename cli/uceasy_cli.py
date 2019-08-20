import click

from uceasy.context import Context
from uceasy.interactor import Interactor


@click.command()
@click.option('--input', required=True)
@click.option('--output', required=True)
@click.option('--sheet', required=True)
@click.option('--probes', required=True)
@click.option('--aligner', required=True)
@click.option('--percent', required=True, type=float)
@click.option('--adapter-i7', '-i7', required=True)
@click.option('--adapter-i5', '-i5', required=True)
@click.option('--phred33', 'fastq_encoding', flag_value='phred33', default='phred33')
@click.option('--phred64', 'fastq_encoding', flag_value='phred64')
@click.option('--min-len', type=int)
@click.option('--r1-pattern', '-r1')
@click.option('--internal-trimming', flag_value=True, default=False)
@click.option('--r2-pattern', '-r2')
@click.option('--no-merge', flag_value=True, default=False)
@click.option('--single-end', flag_value=True, default=False)
def uceasy(input, output, sheet, probes, aligner, percent, adapter_i7, adapter_i5, internal_trimming, fastq_encoding, min_len, r1_pattern, r2_pattern, no_merge, single_end):

    assembler = 'spades'

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
        Spades
        '''
    )
    
    ctx = Context(input,
                  output,
                  sheet,
                  adapter_i7,
                  adapter_i5,
                  probes,
                  assembler,
                  aligner,
                  False,
                  percent,
                  internal_trimming)

    interactor = Interactor(ctx)
    interactor.run()




