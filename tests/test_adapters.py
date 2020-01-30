import pytest

from uceasy.adapters import ADAPTERS


def test_match_contigs_to_probes():
    c = ADAPTERS["match_contigs_to_probes"]("--help")
    assert c.returncode == 0
