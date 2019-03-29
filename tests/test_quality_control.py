import phyluce_facade.phyluce_controller as facade


def test_prepare_inputs_for_template():
    adapter_i5 = 'AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG'
    adapter_i7 = 'AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT'
    sample_sheet = None

    completed_process = facade.run_quality_control(sample_sheet, adapter_i5, adapter_i7)

    assert completed_process.returncode == 0


def test_run_illumiprocessor():
    assert False
