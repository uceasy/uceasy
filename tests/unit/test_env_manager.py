import pytest
import os
import shutil
import pandas as pd


from uceasy.controller import env_manager


OUTPUT = 'testoutput/env_manager_test'
DATA = 'testdata'
SAMPLES = ['alligator_mississippiensis_GGAGCTATGG', 'anolis_carolinensis_GGCGAAGGTT']
SHEET = 'testdata/sample_sheet.csv'


def test_create_output_dir():
    if os.path.isdir(f'{os.getcwd()}/{OUTPUT}'):
        shutil.rmtree(f'{os.getcwd()}/{OUTPUT}')

    env_manager.create_output(OUTPUT)

    assert os.path.isdir(OUTPUT)


def test_fail_if_output_already_exists():

    with pytest.raises(IOError):
        env_manager.create_output(OUTPUT)


def test_conf_file_rendered():
    file = OUTPUT + '/assembly.conf'

    config_dict = {
                'samples': {
                    'sample0': f'{os.getcwd()}/sample/clean_fastq/sample0/split-adapter-quality-trimmed/'
                    }
            }

    env_manager.render_conf_file(file , config_dict)

    assert os.path.isfile(file)


def test_get_samples_names():
    sheet_samples = env_manager.get_samples_from_csv(DATA + '/sample_sheet.csv') 

    assert SAMPLES == sheet_samples

