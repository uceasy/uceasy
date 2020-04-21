from typing import List
import os


"""
For the csv table columns the following is assumed:
0 - The samples' file names.
1 - The i7 barcodes.
2 - The i5 barcodes.
3 - i7 adapter. (first row only)
4 - i5 adapter. (first row only)
"""


def parse_illumiprocessor_config(
    csv_rows: List[str], double_index: bool = True
) -> dict:
    """Read the csv content and creates the illumiprocessor configuration into
    a dictionary to be read by ConfigParser.
    see: https://illumiprocessor.readthedocs.io/en/latest
    /usage.html#creating-a-configuration-file

    :param csv_rows         rows of the csv table.
    :param double_index     type of indexing of the illumina library.
    :return:                A dictionary to be read by ConfigParser.
    """
    config = dict()
    config["adapters"] = {"i7": csv_rows[0][3], "i5": csv_rows[0][4]}
    config["tag sequences"] = dict()
    config["tag map"] = dict()
    config["names"] = dict()

    for index, row in enumerate(csv_rows):
        tag_name_i7 = f"sample{index}_barcode_i7"
        tag_name_i5 = f"sample{index}_barcode_i5"

        config["tag sequences"][tag_name_i7] = row[1]
        config["tag map"][row[0]] = tag_name_i7
        config["names"][row[0]] = row[0]
        if double_index:
            config["tag sequences"][tag_name_i5] = row[2]
            config["tag map"][row[0]] = f"{tag_name_i7},{tag_name_i5}"

    return config


def parse_assembly_config(illumiprocessor_output_dir: str) -> dict:
    """Read the csv content and creates the assembly configuration into
    a dictionary to be read by ConfigParser.
    see: https://phyluce.readthedocs.io/en/latest/assembly.html

    :param illumiprocessor_output_dir   directory of the clean fastq files
        processed previously by illumiprocessor.
    :return:                            A dictionary to be read by ConfigParser.
    """
    config = dict()
    config["samples"] = dict()
    samples = os.listdir(illumiprocessor_output_dir)

    for sample in samples:
        config["samples"][sample] = (
            f"{os.getcwd()}/{illumiprocessor_output_dir}/"
            f"{sample}/split-adapter-quality-trimmed/"
        )

    return config


def parse_taxon_list_config(contigs: str, taxon_group: str) -> str:
    config = f"[{taxon_group}]"
    names = [name for name in os.listdir(contigs)]
    for name in names:
        if name.endswith(".contigs.fasta"):
            name = name[:-14]
            config += f"\n{name}"
    return config
