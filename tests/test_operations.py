import pytest
import os

from uceasy.operations import (
    parse_illumiprocessor_config,
    parse_assembly_config,
)
from uceasy.ioutils import load_csv


@pytest.fixture
def config(context):
    csv_file = load_csv(context["csv_file"])
    config = parse_illumiprocessor_config(csv_file)
    return config


@pytest.fixture
def config_single_index(context):
    csv_file = load_csv(context["csv_file"])
    config = parse_illumiprocessor_config(csv_file, double_index=False)
    return config


@pytest.fixture
def config_assembly(context):
    config = parse_assembly_config(context["clean_fastq"])
    return config


def test_illumiprocessor_config_dict_has_adapters(context, config):
    assert config["adapters"]["i7"] == context["i7_adapter"]
    assert config["adapters"]["i5"] == context["i5_adapter"]


def test_illumiprocessor_config_has_tag_sequences(context, config):
    assert config["tag sequences"]["sample0_barcode_i7"] == context["sample0_barcode_i7"]
    assert config["tag sequences"]["sample0_barcode_i5"] == context["sample0_barcode_i5"]
    assert config["tag sequences"]["sample1_barcode_i7"] == context["sample1_barcode_i7"]
    assert config["tag sequences"]["sample1_barcode_i5"] == context["sample1_barcode_i5"]


def test_illumiprocessor_config_single_index_tag_sequences(context, config_single_index):
    assert (
        config_single_index["tag sequences"]["sample0_barcode_i7"] == context["sample0_barcode_i7"]
    )
    assert (
        config_single_index["tag sequences"]["sample1_barcode_i7"] == context["sample1_barcode_i7"]
    )
    assert "sample0_barcode_i5" not in config_single_index["tag sequences"]
    assert "sample1_barcode_i5" not in config_single_index["tag sequences"]


def test_illumiprocessor_config_has_tag_map(context, config):
    assert config["tag map"][context["sample0"]] == "sample0_barcode_i7,sample0_barcode_i5"
    assert config["tag map"][context["sample1"]] == "sample1_barcode_i7,sample1_barcode_i5"


def test_illumiprocessor_config_single_index_tag_map(context, config_single_index):
    assert config_single_index["tag map"][context["sample0"]] == "sample0_barcode_i7"
    assert config_single_index["tag map"][context["sample1"]] == "sample1_barcode_i7"


def test_illumiprocessor_config_has_names(context, config):
    assert config["names"][context["sample0"]] == context["sample0"]
    assert config["names"][context["sample1"]] == context["sample1"]


def test_assembly_config_has_samples(context, config_assembly):
    assert (
        f"{os.getcwd()}/{context['clean_fastq']}/"
        f"{context['sample0']}/split-adapter-quality-trimmed/"
    ) in config_assembly["samples"][context["sample0"]]
    assert (
        f"{os.getcwd()}/{context['clean_fastq']}/"
        f"{context['sample1']}/split-adapter-quality-trimmed/"
    ) in config_assembly["samples"][context["sample1"]]
