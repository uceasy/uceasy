from types import SimpleNamespace

from uceasy.facade import AssemblyFacade, QualityControlFacade, UCEPhylogenomicsFacade
from uceasy.tracking import save_tracking_file


def run_quality_control(context: SimpleNamespace):
    save_tracking_file(QualityControlFacade(context).run())


def run_assembly(context: SimpleNamespace):
    save_tracking_file(AssemblyFacade(context).run())


def run_phylogenomics(context: SimpleNamespace):
    save_tracking_file(PhylogenomicsFacade(context).run())
