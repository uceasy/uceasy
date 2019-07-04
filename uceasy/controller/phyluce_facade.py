from uceasy.adapters import assembly
from uceasy.adapters import quality_control
from uceasy.controller import env_manager


class Facade:


    def __init__(self, context):
        self.__context = context


    def quality_control(self):

        config_dict = env_manager.prepare_illumiprocessor_conf(self.__context.sheet,
                                                               self.__context.adapter_i7,
                                                               self.__context.adapter_i5)

        config = env_manager.render_conf_file('illumiprocessor.conf', self.__context.output, config_dict)

        return quality_control.run_illumiprocessor(config, context.input,
                                                   context.output + '/illumiprocessor')


    def assembly(self):
        config_dict = env_manager.prepare_assembly_conf(self.__samples)
        config = env_manager.render_conf_file('assembly.conf', self.__context.output, config_dict)

        return assembly.run_trinity(config, self.__context.output + '/assembly')


    def uce_processing():
        pass
