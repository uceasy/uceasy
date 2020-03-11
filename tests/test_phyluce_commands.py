from uceasy.ioutils import run_command


DATA = "testdata"
OUT = "testoutput"


def test_match_contigs_to_probes():
    cmd = run_command("phyluce_assembly_match_contigs_to_probes", "help")
    assert cmd.returncode == 0


def test_illumiprocessor():
    cmd = run_command("illumiprocessor", "help")
    assert cmd.returncode == 0
