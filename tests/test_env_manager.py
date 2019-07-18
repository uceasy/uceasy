from uceasy.controller import env_manager
import pytest
from tests import OUTPUT
import os



def test__conf_file_rendered():
    output = OUTPUT + '/assembly.conf'
    config_dict = {
                'samples': {
                    'sample0': f'{os.getcwd()}/sample/clean_fastq/sample0/split-adapter-quality-trimmed/'
                    }
            }

    env_manager.render_conf_file(output, config_dict)

    assert os.path.isfile(output)


def test_create_output_dir():
    output = OUTPUT + '/test_output'
    env_manager.create_output(output)

    assert os.path.isdir(output)


def test_fail_if_output_already_exists():
    output = OUTPUT + '/test_output'

    with pytest.raises(IOError):
        env_manager.create_output(output)

