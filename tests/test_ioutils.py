import pytest

from uceasy.ioutils import load_csv, dump_config_file


@pytest.fixture
def config_example():
    config = {
        "adapters": {
            "i7": "AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG",
            "i5": "AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT",
        }
    }
    expected = """[adapters]
i7:AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG
i5:AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT

"""
    return (config, expected)


@pytest.fixture
def config_novalue():
    config = {"samples": {"sample1": None, "sample2": None}}
    expected = """[samples]
sample1
sample2

"""
    return (config, expected)


def test_load_csv_returns_a_list(context):
    csv = load_csv(context["csv_file"])
    assert isinstance(csv, list)


def test_config_file_is_created(context, config_example):
    dump_config_file(context["output"] + "test.conf", config_example[0])
    with open(context["output"] + "test.conf", "r") as fl:
        assert fl.read() == config_example[1]
