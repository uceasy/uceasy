import pandas as pd
import itertools
import configparser
from controller import WORKENV


def render_conf_file(name, config_dict):
    config     = WORKENV + name
    configfile = configparser.ConfigParser(delimiters=(':'))

    configfile.optionxform = str
    configfile.read_dict(config_dict)

    with open(config, 'w') as fl:
        configfile.write(fl, space_around_delimiters=False)

    return config


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

    config_dict['tag sequences'] = {k: v for k, v in itertools.chain(tags_i5.items(), tags_i7.items())}

    config_dict['tag map'] = {row['Customer_Code']: f"{row['i5_Tag']},{row['i7_Tag']}"
                              for _, row in sheet.iterrows()}

    config_dict['names'] = {row['Customer_Code']: f'sample{index}'
                            for index, row in sheet.iterrows()}

    return config_dict
