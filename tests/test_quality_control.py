from uceasy.controller.phyluce_facade import Facade
from tests import CONTEXT


def test_run_quality_control():
    facade = Facade(CONTEXT)
    cmd = facade.quality_control()
    assert cmd.returncode == 0

