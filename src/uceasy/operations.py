from typing import List


def parse_illumiprocessor_config(
    csv_rows: List[str], double_index: bool = True
) -> dict:
    """Read the csv content and creates the illumiprocessor configuration into
    a dictionary to be read by ConfigParser.
    see: https://illumiprocessor.readthedocs.io/en/latest
    /usage.html#creating-a-configuration-file

    For the table columns the following is assumed:
    0 - The samples' file names.
    1 - The i7 barcodes.
    2 - The i5 barcodes.
    3 - i7 adapter. (only first row necessary)
    4 - i5 adapter. (only first row necessary)

    :param csv_rows         rows of the csv table.
    :param double_index     type of indexing of the illumina library.
    :return:                A dictionary to be read by ConfigParser.
    """
    config_dict = dict()
    config_dict["adapters"] = {"i7": csv_rows[0][3], "i5": csv_rows[0][4]}
    config_dict["tag sequences"] = dict()
    config_dict["tag map"] = dict()
    config_dict["names"] = dict()

    for index, row in enumerate(csv_rows):
        tag_name_i7 = f"sample{index}_barcode_i7"
        tag_name_i5 = f"sample{index}_barcode_i5"

        config_dict["tag sequences"][tag_name_i7] = row[1]
        config_dict["tag map"][row[0]] = tag_name_i7
        config_dict["names"][row[0]] = row[0]
        if double_index:
            config_dict["tag sequences"][tag_name_i5] = row[2]
            config_dict["tag map"][row[0]] = f"{tag_name_i7},{tag_name_i5}"

    return config_dict
