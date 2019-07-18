from uceasy.adapters import assembly


CONFIG = 'sample/assembly.conf'


def test_if_trinity_is_running():
    cmd = assembly.run_trinity(CONFIG, CONTEXT.output + '/trinity')
    assert cmd.returncode == 0


def test_if_spades_is_running():
    cmd = assembly.run_spades(CONFIG, CONTEXT.output + '/spades')
    assert cmd.returncode == 0
