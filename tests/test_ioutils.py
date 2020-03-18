import os.path

from uceasy.ioutils import load_csv, dump_config_file


CSV = "testdata/sample_sheet.csv"
CONFIG = {
    "adapters": {
        "i7": "AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG",
        "i5": "AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT",
    }
}
OUT = "testoutput/"


def test_load_csv_returns_a_list():
    csv = load_csv(CSV)
    assert isinstance(csv, list)


def test_config_file_is_created():
    dump_config_file(OUT + "test.conf", CONFIG)
    assert os.path.isfile(OUT + "test.conf")
