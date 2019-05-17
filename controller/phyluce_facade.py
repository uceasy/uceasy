import os
from adapters.assembly import run_trinity
from adapters.quality_control import run_illumiprocessor
from controller.env_manager import render_conf_file, prepare_illumiprocessor_conf
from controller import CLEAN_FASTQ, TRINITY_ASSEMBLIES


def run_quality_control(input, sheet, adapter_i7, adapter_i5):
    config_dict = prepare_illumiprocessor_conf(sheet, adapter_i7, adapter_i5)
    config      = render_conf_file('illumiprocessor.conf', config_dict)

    return run_illumiprocessor(config, input, CLEAN_FASTQ)


def run_assembly():
    pass
