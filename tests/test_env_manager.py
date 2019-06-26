from uceasy.controller.env_manager import render_conf_file
from uceasy.controller import WORKENV
from tests import PATH
import os


def test_should_pass_when_conf_file_rendered():
    config_dict = {
                'samples': {
                        'sample0': f'{PATH}/sample/clean_fastq/sample0/split-adapter-quality-trimmed/'
                    }
            }

    render_conf_file('assembly.conf', config_dict)

    assert os.path.isfile(WORKENV + 'assembly.conf')


def test_prepare_illumiprocessor_conf():
    assert False


def test_prepare_assembly_conf():
    assert False
