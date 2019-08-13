from uceasy.adapters import assembly
from uceasy.controller import env_manager
import os


sample = os.getcwd() + '/testdata/clean-fastq/sample0/split-adapter-quality-trimmed'
output = os.getcwd() + '/testoutput'


config_dict = { 'samples': { 'sample': sample } }
config = env_manager.render_conf_file(output + '/assembly.conf', config_dict)


def test_if_trinity_is_running():
    cmd = assembly.run_trinity(config, output + '/trinity')
    assert cmd.returncode == 0


def test_if_spades_is_running():
    cmd = assembly.run_spades(config, output + '/spades')
    assert cmd.returncode == 0

