from uceasy.controller.phyluce_facade import  Facade
import subprocess
import os


output = os.getcwd() + '/sample/output'
sheet = 'sample/sample_sheet.csv',
adapter_i7 = 'AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG'
adapter_i5 = 'AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT'
samples = ['alligator']


def test_run_quality_control():
    facade = Facade()
    cmd = facade.quality_control(output, sheet, adapter_i7, adapter_i5)

    assert isinstance(cmd, subprocess.CompletedProcess)


def test_assembly():
    facade = Facade()
    cmd = facade.assembly(output, samples)

    assert isinstance(cmd, subprocess.CompletedProcess)

