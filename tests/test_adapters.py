from uceasy.adapters import ADAPTERS


def test_illumiprocessor_help():
    cmd = ADAPTERS["illumiprocessor"](["--help"], capture_output=True)
    assert "usage: illumiprocessor" in cmd[0]


def test_trinity_help():
    cmd = ADAPTERS["trinity"](["--help"], capture_output=True)
    assert "usage: phyluce_assembly_assemblo_trinity" in cmd[0]
