from uceasy.controller import env_manager
import pytest
import os
import shutil


output = 'testdata/output/test_output'


def test_create_output_dir():
    if os.path.isdir(f'{os.getcwd()}/{output}'):
        shutil.rmtree(f'{os.getcwd()}/{output}')

    env_manager.create_output(output)

    assert os.path.isdir(output)


def test_fail_if_output_already_exists():

    with pytest.raises(IOError):
        env_manager.create_output(output)


def test_conf_file_rendered():
    file = output + '/assembly.conf'

    config_dict = {
                'samples': {
                    'sample0': f'{os.getcwd()}/sample/clean_fastq/sample0/split-adapter-quality-trimmed/'
                    }
            }

    env_manager.render_conf_file(file , config_dict)

    assert os.path.isfile(file)


