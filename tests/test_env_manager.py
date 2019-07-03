from uceasy.controller.env_manager import render_conf_file
from uceasy.context import Context
import os


CONTEXT = Context(input='sample/raw_fastq',
                  output= os.getcwd() + '/data',
                  sheet='sample/alligator_sheet.csv',
                  adapter_i5='AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG',
                  adapter_i7='AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT')


def test_should_pass_when_conf_file_rendered():
    config_dict = {
                'samples': {
                        'sample0': f'{os.getcwd()}/sample/clean_fastq/sample0/split-adapter-quality-trimmed/'
                    }
            }

    render_conf_file('assembly.conf', CONTEXT.output, config_dict)

    assert os.path.isfile(CONTEXT.output + '/assembly.conf')


def test_prepare_illumiprocessor_conf():
    assert False


def test_prepare_assembly_conf():
    assert False
