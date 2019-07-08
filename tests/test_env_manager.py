from uceasy.controller.env_manager import render_conf_file
from tests import CONTEXT
import os


def test_should_pass_when_conf_file_rendered():
    config_dict = {
                'samples': {
                        'sample0': f'{os.getcwd()}/sample/clean_fastq/sample0/split-adapter-quality-trimmed/'
                    }
            }

    render_conf_file('assembly.conf', CONTEXT.output, config_dict)

    assert os.path.isfile(CONTEXT.output + '/assembly.conf')

