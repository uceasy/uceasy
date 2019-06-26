from uceasy.adapters import assembly


CONFIG = 'sample/assembly.conf'


def test_if_trinity_is_running():
    cmd = assembly.run_trinity(CONFIG, 'data/trinity_assemblies')
    assert cmd.returncode == 0


def test_if_spades_is_running():
    cmd = assembly.run_spades(CONFIG, 'data/spades_assemblies')
    assert cmd.returncode == 0
