from uceasy.controller.phyluce_facade import run_quality_control
from uceasy.context import Context
import os


CONTEXT = Context(input='sample/raw_fastq',
                  output= os.getcwd() + '/data',
                  sheet='sample/alligator_sheet.csv',
                  adapter_i5='AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG',
                  adapter_i7='AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT')


def test_run_quality_control():
    cmd = run_quality_control(CONTEXT)
    assert cmd.returncode == 0

