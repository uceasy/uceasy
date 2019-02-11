import pandas as pd
import subprocess
import os
from jinja2 import Environment, FileSystemLoader
from facade import WORKENV, INPUT, OUTPUT, TRIMMOMATIC, CPU


def prepare_inputs_for_template(sheet, adapter_i5, adapter_i7):
    sheet = sheet[sheet.columns[1:4]]
    sheet['i5_Tag'] = pd.Series([f"sample{index}_barcode_i5" for index in sheet.index.values])
    sheet['i7_Tag'] = pd.Series([f"sample{index}_barcode_i7" for index in sheet.index.values])

    adapters = ["i5:" + adapter_i5, "i7:" + adapter_i7]

    tags_i5 = [f"{row['i5_Tag']}:{row['i5_Barcode_Seq']}" for _, row in sheet.iterrows()]
    tags_i7 = [f"{row['i7_Tag']}:{row['i7_Barcode_Seq']}" for _, row in sheet.iterrows()]
    tag_sequences = sorted(tags_i5 + tags_i7)

    tag_maps = [f"{row['Customer_Code']}:{row['i5_Tag']},{row['i7_Tag']}" for _, row in sheet.iterrows()]

    names = [f"{row['Customer_Code']}:sample{index}" for index, row in sheet.iterrows()]

    return adapters, tag_sequences, tag_maps, names


def render_conf_file(adapters, tag_sequences, tag_maps, names):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('illumiprocessor.txt')
    conf_path = WORKENV + 'illumiprocessor.conf'

    with open(conf_path, 'w') as conf_file:
        settings = template.render(adapters=adapters, tag_sequences=tag_sequences, tag_maps=tag_maps, names=names)
        conf_file.write(settings)

    if os.path.isfile(conf_path):
        return conf_path
    raise IOError('illumiprocessor.conf was not generated')


def run_illumiprocessor():
    cmd = [
        'illumiprocessor',
        '--input', INPUT,
        '--output', OUTPUT,
        '--config', CONF_FILE,
        '--cores', CPU,
        '--trimmomatic', TRIMMOMATIC
    ]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        pass
