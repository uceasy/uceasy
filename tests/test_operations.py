import pytest
import os

from uceasy.operations import (
    parse_illumiprocessor_config,
    parse_assembly_config,
)
from uceasy.ioutils import load_csv


CSV = "testdata/sample_sheet.csv"
# Same content as in CSV
I7_ADAPTER = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG"
I5_ADAPTER = "AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT"
SAMPLE0 = "alligator_mississippiensis_GGAGCTATGG"
SAMPLE1 = "anolis_carolinensis_GGCGAAGGTT"
SAMPLE0_BARCODE_I7 = "GGAGCTATGG"
SAMPLE0_BARCODE_I5 = "GGAGCTATGG"
SAMPLE1_BARCODE_I7 = "GGCGAAGGTT"
SAMPLE1_BARCODE_I5 = "GGCGAAGGTT"

ILLUMIPROCESSOR_OUTPUT = "testdata/clean-fastq"


@pytest.fixture
def config():
    csv_file = load_csv(CSV)
    config = parse_illumiprocessor_config(csv_file)
    return config


@pytest.fixture
def config_single_index():
    csv_file = load_csv(CSV)
    config = parse_illumiprocessor_config(csv_file, double_index=False)
    return config


@pytest.fixture
def config_assembly():
    csv_file = load_csv(CSV)
    config = parse_assembly_config(ILLUMIPROCESSOR_OUTPUT)
    return config


def test_illumiprocessor_config_dict_has_adapters(config):
    assert config["adapters"]["i7"] == I7_ADAPTER
    assert config["adapters"]["i5"] == I5_ADAPTER


def test_illumiprocessor_config_has_tag_sequences(config):
    assert config["tag sequences"]["sample0_barcode_i7"] == SAMPLE0_BARCODE_I7
    assert config["tag sequences"]["sample0_barcode_i5"] == SAMPLE0_BARCODE_I5
    assert config["tag sequences"]["sample1_barcode_i7"] == SAMPLE1_BARCODE_I7
    assert config["tag sequences"]["sample1_barcode_i5"] == SAMPLE1_BARCODE_I5


def test_illumiprocessor_config_single_index_tag_sequences(config_single_index):
    assert (
        config_single_index["tag sequences"]["sample0_barcode_i7"]
        == SAMPLE0_BARCODE_I7
    )
    assert (
        config_single_index["tag sequences"]["sample1_barcode_i7"]
        == SAMPLE1_BARCODE_I7
    )
    assert "sample0_barcode_i5" not in config_single_index["tag sequences"]
    assert "sample1_barcode_i5" not in config_single_index["tag sequences"]


def test_illumiprocessor_config_has_tag_map(config):
    assert config["tag map"][SAMPLE0] == "sample0_barcode_i7,sample0_barcode_i5"
    assert config["tag map"][SAMPLE1] == "sample1_barcode_i7,sample1_barcode_i5"


def test_illumiprocessor_config_single_index_tag_map(config_single_index):
    assert config_single_index["tag map"][SAMPLE0] == "sample0_barcode_i7"
    assert config_single_index["tag map"][SAMPLE1] == "sample1_barcode_i7"


def test_illumiprocessor_config_has_names(config):
    assert config["names"][SAMPLE0] == SAMPLE0
    assert config["names"][SAMPLE1] == SAMPLE1


def test_assembly_config_has_samples(config_assembly):
    assert (
        f"{os.getcwd()}/{ILLUMIPROCESSOR_OUTPUT}/"
        f"{SAMPLE0}/split-adapter-quality-trimmed/"
    ) in config_assembly["samples"][SAMPLE0]
    assert (
        f"{os.getcwd()}/{ILLUMIPROCESSOR_OUTPUT}/"
        f"{SAMPLE1}/split-adapter-quality-trimmed/"
    ) in config_assembly["samples"][SAMPLE1]
