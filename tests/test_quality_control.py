from uceasy.controller.phyluce_facade import  Facade
from tests import OUTPUT


sheet = 'sample/sample_sheet.csv',
adapter_i7 = 'AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG'
adapter_i5 = 'AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT'


def test_run_quality_control():
    facade = Facade()
    cmd = facade.quality_control(OUTPUT, sheet, adapter_i7, adapter_i5)
    assert cmd.returncode == 0

