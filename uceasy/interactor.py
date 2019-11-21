from uceasy.controller.facade import Facade
from uceasy.controller import env_manager


class Interactor:
    def __init__(self, context):
        self.__context = context
        self.__facade = Facade()

    def run(self):

        samples = env_manager.get_samples_from_csv(self.__context.sheet)

        self.__facade.quality_control(
            self.__context.input,
            self.__context.output,
            self.__context.sheet,
            self.__context.adapter_i7,
            self.__context.adapter_i5,
        )

        self.__facade.assembly(self.__context.output, self.__context.assembler, samples)

        contigs = self.__context.output + "/assembly/contigs"

        self.__facade.process_uce(
            self.__context.output,
            self.__context.output,
            contigs,
            self.__context.probes,
            samples,
            self.__context.aligner,
            self.__context.charsets,
            self.__context.percent,
            self.__context.internal_trimming,
        )
