import pytest

from uceasy import adapters


def test_if_current_conda_environment_is_phyluce():
    out = str(adapters.run("conda list").stdout)

    assert "phyluce" in out
