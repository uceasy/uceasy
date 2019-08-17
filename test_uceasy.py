from uceasy.context import Context
from uceasy.interactor import Interactor


ctx = Context('testdata/raw-fastq',
              'testoutput',
              'testdata/sample_sheet.csv',
              'AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG',
              'AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT',
              'testdata/probes.fasta',
              'spades',
              'mafft',
              False,
              '0.75',
              True)

interactor = Interactor(ctx)
interactor.run()
