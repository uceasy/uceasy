from controller.phyluce_facade import run_assembly


def test_run_assembly():
    cmd = run_assembly()
    assert cmd.returncode == 0 
