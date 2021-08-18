import pytest

from uceasy.adapters import Adapters


@pytest.fixture
def adapters():
    return Adapters().adapters


def test_illumiprocessor_help(adapters):
    cmd = adapters["illumiprocessor"](["--help"])
    assert "usage: illumiprocessor" in cmd[0]


def test_trinity_help(adapters):
    cmd = adapters["trinity"](["--help"])
    assert "usage: phyluce_assembly_assemblo_trinity" in cmd[0]


def test_spades_help(adapters):
    cmd = adapters["spades"](["--help"])
    assert "usage: phyluce_assembly_assemblo_spades" in cmd[0]


def test_match_contigs_to_probes_help(adapters):
    cmd = adapters["match_contigs_to_probes"](["--help"])
    assert "usage: phyluce_assembly_match_contigs_to_probes" in cmd[0]
