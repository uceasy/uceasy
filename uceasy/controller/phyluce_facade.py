from uceasy.adapters import assembly
from uceasy.adapters import quality_control
from uceasy.controller import env_manager


class Facade:


    def quality_control(self, input, output, sheet, adapter_i7, adapter_i5):

        config_dict = env_manager.prepare_illumiprocessor_conf(sheet,
                                                               adapter_i7,
                                                               adapter_i5)

        config = env_manager.render_conf_file(output + '/illumiprocessor.conf', config_dict)

        return quality_control.run_illumiprocessor(input,
                                                   output + '/illumiprocessor', config)


    def assembly(self, output, samples, assembler):
        config_dict = env_manager.prepare_assembly_conf(output, samples)
        config = env_manager.render_conf_file(output + '/assembly.conf', config_dict)

        return assembly.run_trinity(config, output + '/assembly')


    def process_uce(self):
        pass
