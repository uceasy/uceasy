import pandas as pd
import os
import configparser


def render_conf_file(file, config_dict):

    parser = configparser.ConfigParser(delimiters=(':'))
    parser.optionxform = str
    parser.read_dict(config_dict)

    with open(file, 'w') as fl:
        parser.write(fl, space_around_delimiters=False)

    return file


def prepare_illumiprocessor_conf(sheet, adapter_i7, adapter_i5):
    config_dict = dict()
    sheet = pd.read_csv(sheet)
    sheet = sheet[sheet.columns[1:4]]

    sheet['i5_Tag'] = pd.Series([
        f"sample{index}_barcode_i5"
        for index in sheet.index.values
    ])
    sheet['i7_Tag'] = pd.Series([
        f"sample{index}_barcode_i7"
        for index in sheet.index.values
    ])

    config_dict['adapters'] = {"i7": adapter_i7, "i5": adapter_i5}

    tags_i5 = {row['i5_Tag']: row['i5_Barcode_Seq']
               for _, row in sheet.iterrows()}

    tags_i7 = {row['i7_Tag']: row['i7_Barcode_Seq']
               for _, row in sheet.iterrows()}

    config_dict['tag sequences'] = {**tags_i5, **tags_i7}

    config_dict['tag map'] = {row['Customer_Code']: f"{row['i5_Tag']},{row['i7_Tag']}"
                              for _, row in sheet.iterrows()}

    config_dict['names'] = {row['Customer_Code']: f'sample{index}'
                            for index, row in sheet.iterrows()}
    return config_dict


def prepare_assembly_conf(output, samples):
    config_dict = dict()
    config_dict['samples'] = {sample: f'{output}/illumiprocessor/{sample}/split-adapter-quality-trimmed/'
                              for sample in samples}
    return config_dict


def get_samples(sheet):
    # TODO
    # get sample names from csv file
    pass


def create_output(output):
    output = f'{os.getcwd()}/{output}'
    if os.path.isdir(output):
        raise IOError('Error: output directory already exists!\n'
                      'Rename or remove it before running UCEasy.')
    os.mkdir(output)
