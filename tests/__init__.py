from uceasy.context import Context
import os


CONTEXT = Context(input='tests/raw_fastq',
                  output='tests/output',
                  sheet='tests/sample_sheet.csv',
                  adapter_i7='AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG',
                  adapter_i5='AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT',
                  probes='tests/probes',
                  assembler='trinity')


