from uceasy.controller.phyluce_facade import Facade
from tests import CONTEXT


def test_assembly():
    facade = Facade(CONTEXT)
    cmd = facade.assembly()
    assert cmd.returncode == 0

