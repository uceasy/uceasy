from uceasy.context import Context
import os


context = Context(input='sample/raw_fastq',
                  output='sample/output',
                  sheet='sample/sample_sheet.csv',
                  adapter_i7='AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG',
                  adapter_i5='AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT',
                  probes='samples/probes',
                  assembler='trinity')

