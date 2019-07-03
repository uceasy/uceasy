from uceasy.adapters import assembly
from uceasy.adapters import quality_control
from uceasy.controller import env_manager


def run_quality_control(context):

    config_dict = env_manager.prepare_illumiprocessor_conf(context.sheet,
                                                           context.adapter_i7,
                                                           context.adapter_i5)
    config = env_manager.render_conf_file('illumiprocessor.conf', context.output, config_dict)

    return quality_control.run_illumiprocessor(config, context.input, context.output + '/illumiprocessor')


def run_assembly(context):
    config_dict = env_manager.prepare_assembly_conf(context)
    config = env_manager.render_conf_file('assembly.conf', context.output, config_dict)

    return assembly.run_trinity(config, context.output + '/assembly')


def run_uce_processing():
    pass
