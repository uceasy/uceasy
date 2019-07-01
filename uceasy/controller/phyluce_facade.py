from uceasy.adapters import assembly
from uceasy.adapters import quality_control
from uceasy.controller import env_manager
from uceasy.controller import CLEAN_FASTQ, TRINITY_ASSEMBLIES


def run_quality_control(input, sheet, adapter_i7, adapter_i5):

    config_dict = env_manager.prepare_illumiprocessor_conf(sheet, adapter_i7, adapter_i5)
    config = env_manager.render_conf_file('illumiprocessor.conf', config_dict)

    return quality_control.run_illumiprocessor(config, input, CLEAN_FASTQ)


def run_assembly():

    config_dict = env_manager.prepare_assembly_conf()
    config = env_manager.render_conf_file('assembly.conf', config_dict)

    return assembly.run_trinity(config, TRINITY_ASSEMBLIES)


def run_uce_processing():
    pass
