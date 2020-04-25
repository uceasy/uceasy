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
    csv = load_csv(context["csv"])
    assert isinstance(csv, list)


def test_config_file_is_created(context, config_example):
    dump_config_file(context["output"] + "test.conf", config_example[0])
    with open(context["output"] + "test.conf", "r") as fl:
        assert fl.read() == config_example[1]


def test_allow_no_value(context, config_novalue):
    dump_config_file(
        context["output"] + "novalue.conf",
        config_novalue[0],
        allow_no_value=True,
    )
    with open(context["output"] + "novalue.conf", "r") as fl:
        assert fl.read() == config_novalue[1]


def test_raises_typeerror_if_allow_no_value_is_false(context):
    with pytest.raises(TypeError):
        dump_config_file(
            context["output"] + "novalue.conf", config_novalue[0],
        )
