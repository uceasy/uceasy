import pytest

from uceasy.operations import parse_illumiprocessor_config
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


@pytest.fixture
def config():
    csv_file = load_csv(CSV)
    config = parse_illumiprocessor_config(csv_file)
    return config


def test_illumiprocessor_config_dict_has_adapters(config):
    assert "adapters" in config
    assert config["adapters"]["i7"] == I7_ADAPTER
    assert config["adapters"]["i5"] == I5_ADAPTER


def test_illumiprocessor_config_has_tag_sequences(config):
    assert "tag sequences" in config
    assert config["tag sequences"]["sample0_barcode_i7"] == SAMPLE0_BARCODE_I7
    assert config["tag sequences"]["sample0_barcode_i5"] == SAMPLE0_BARCODE_I5
    assert config["tag sequences"]["sample1_barcode_i7"] == SAMPLE1_BARCODE_I7
    assert config["tag sequences"]["sample1_barcode_i5"] == SAMPLE1_BARCODE_I5


def test_illumiprocessor_config_has_tag_map(config):
    assert "tag map" in config
    assert config["tag map"][SAMPLE0] == "sample0_barcode_i7,sample0_barcode_i5"
    assert config["tag map"][SAMPLE1] == "sample1_barcode_i7,sample1_barcode_i5"


def test_illumiprocessor_config_has_names(config):
    assert "names" in config
    assert config["names"][SAMPLE0] == SAMPLE0.lower()
    assert config["names"][SAMPLE1] == SAMPLE1.lower()
