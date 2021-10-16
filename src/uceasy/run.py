from types import SimpleNamespace

from uceasy.facade import AssemblyFacade, QualityControlFacade, UCEAlignmentFacade
from uceasy.tracking import save_tracking_file


def run_quality_control(context: SimpleNamespace):
    fl = context.log_dir + context.tracking_file
    save_tracking_file(fl, QualityControlFacade(context).run())


def run_assembly(context: SimpleNamespace):
    fl = context.log_dir + context.tracking_file
    save_tracking_file(fl, AssemblyFacade(context).run())


def run_alignment(context: SimpleNamespace):
    fl = context.log_dir + context.tracking_file
    save_tracking_file(fl, UCEAlignmentFacade(context).run())
