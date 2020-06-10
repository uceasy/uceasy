import pytest
import shutil
import os


# This data is in pair with the contents of "testdata/sheet.csv"
# I know this might not be the best approach for testing the config files,
# please open a issue if you have a better idea.
test_context = {
    "output": "testoutput/",
    "csv": "testdata/sheet.csv",
    "raw_fastq": "testdata/raw-fastq/",
    "clean_fastq": "testdata/clean-fastq/",
    "contigs": "testdata/spades-assemblies/contigs/",
    "probes": "testdata/probes.fasta",
    "i7_adapter": "AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG",
    "i5_adapter": "AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT",
    "sample0": "alligator_mississippiensis_GGAGCTATGG",
    "sample1": "anolis_carolinensis_GGCGAAGGTT",
    "sample0_barcode_i7": "GGAGCTATGG",
    "sample0_barcode_i5": "GGAGCTATGG",
    "sample1_barcode_i7": "GGCGAAGGTT",
    "sample1_barcode_i5": "GGCGAAGGTT",
}


if not os.path.isdir(test_context["output"]):
    os.mkdir(test_context["output"])
else:
    shutil.rmtree(test_context["output"])
    os.mkdir(test_context["output"])


@pytest.fixture
def context():
    return test_context


def pytest_configure(config):
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")
