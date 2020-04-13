import os
import pytest

from uceasy.ioutils import load_csv, dump_config_file


@pytest.fixture
def config_example():
    return {
        "adapters": {
            "i7": "AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG",
            "i5": "AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT",
        }
    }


def test_load_csv_returns_a_list(context):
    csv = load_csv(context["csv"])
    assert isinstance(csv, list)


def test_config_file_is_created(context, config_example):
    dump_config_file(context["output"] + "test.conf", config_example)
    assert os.path.isfile(context["output"] + "test.conf")
