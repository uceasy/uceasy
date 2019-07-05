from uceasy.context import Context
import os


input = f'{os.getcwd()}/sample/raw_fastq'
output = f'{os.getcwd()}/sample/output'


CONTEXT = Context(input=input,
                  output=output,
                  sheet='sample/sample_sheet.csv',
                  adapter_i7='AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG',
                  adapter_i5='AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT',
                  probes='sample/probes/',
                  assembler='trinity')


if not os.path.isdir(output):
    os.mkdir(output)
