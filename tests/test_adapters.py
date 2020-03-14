from uceasy.adapters import ADAPTERS


def test_illumiprocessor():
    cmd = ADAPTERS["illumiprocessor"](["--help"], capture_output=True)
    assert "usage: illumiprocessor" in cmd[0]
