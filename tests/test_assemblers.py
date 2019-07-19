from uceasy.adapters import assembly
import os


output = os.getcwd() + '/testdata/output'
config = os.getcwd() + '/testdata/assembly.conf'


def test_if_trinity_is_running():
    cmd = assembly.run_trinity(config, output + '/trinity')
    assert cmd.returncode == 0


def test_if_spades_is_running():
    cmd = assembly.run_spades(config, output + '/spades')
    assert cmd.returncode == 0

