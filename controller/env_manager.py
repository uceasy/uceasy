from jinja2 import Environment, FileSystemLoader
import os


def render_conf_file(name, template_file, **fields):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_file)

    with open(name, 'w') as file:
        settings = template.render(fields)
        file.write(settings)

    return os.path.isfile(name)
            

def prepare_inputs_for_template(sheet, adapter_i5, adapter_i7):
    sheet = sheet[sheet.columns[1:4]]
    sheet['i5_Tag'] = pd.Series([
        f"sample{index}_barcode_i5"
        for index in sheet.index.values
    ])
    sheet['i7_Tag'] = pd.Series([
        f"sample{index}_barcode_i7"
        for index in sheet.index.values
    ])

    adapters = ["i5:" + adapter_i5, "i7:" + adapter_i7]

    tags_i5 = [
        f"{row['i5_Tag']}:{row['i5_Barcode_Seq']}"
        for _, row in sheet.iterrows()
    ]
    tags_i7 = [
        f"{row['i7_Tag']}:{row['i7_Barcode_Seq']}"
        for _, row in sheet.iterrows()
    ]
    tag_sequences = sorted(tags_i5 + tags_i7)

    tag_maps = [
        f"{row['Customer_Code']}:{row['i5_Tag']},{row['i7_Tag']}"
        for _, row in sheet.iterrows()]

    names = [
        f"{row['Customer_Code']}:sample{index}"
        for index, row in sheet.iterrows()
    ]

    return adapters, tag_sequences, tag_maps, names
