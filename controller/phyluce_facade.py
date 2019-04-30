import os
from adapters.assembly import run_trinity
from adapters.quality_control import run_illumiprocessor
from controller.env_manager import render_illumiprocessor_conf, render_assembly_conf, prepare_inputs_for_template
from controller import CLEAN_FASTQ, TRINITY_ASSEMBLIES


def run_quality_control(input, sheet, adapter_i7, adapter_i5):
    adapters, tag_sequences, tag_maps, names = prepare_inputs_for_template(sheet, adapter_i7, adapter_i5)

    conf_file = render_illumiprocessor_conf('illumiprocessor.conf', 'illumiprocessor.txt',
                                            adapters, tag_sequences, tag_maps, names)
    run_illumiprocessor(conf_file, input, CLEAN_FASTQ)


# TODO
# usuario poder escolher o assembler
def run_assembly():
    samples_names = os.listdir(CLEAN_FASTQ)
    samples = [f'{sample}:{CLEAN_FASTQ}/{sample}/split-adapter-quality-trimmed/'
               for sample in samples_names]
    conf_file = render_assembly_conf('assembly.conf', 'assembly.txt', samples)
    run_trinity(conf_file, TRINITY_ASSEMBLIES)

