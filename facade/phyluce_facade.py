from facade.quality_control import prepare_inputs_for_template, run_illumiprocessor


def run_quality_control(sheet, adapter_i5, adapter_i7):
    adapters, tag_sequences, tag_maps, names = prepare_inputs_for_template(sheet, adapter_i5, adapter_i7)
    return run_illumiprocessor(adapters, tag_sequences, tag_maps, names)


def run_assembly():
    pass
