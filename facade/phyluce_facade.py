import facade.quality_control as qc


def run_quality_control(sheet, adapter_i5, adapter_i7):
    adapters, tag_sequences, tag_maps, names = qc.prepare_inputs_for_template(sheet, adapter_i5, adapter_i7)
    qc.render_conf_file(adapters, tag_sequences, tag_maps, names)
    qc.run_illumiprocessor()


def run_assembly():
    pass
