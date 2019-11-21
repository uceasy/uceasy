from uceasy.context import Context
import os


context = Context(
    input="testdata/raw_fastq",
    output="testoutput",
    sheet="testdata/sample_sheet.csv",
    adapter_i7="AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG",
    adapter_i5="AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT",
    probes="testdata/probes",
    aligner="mafft",
    percent="0.75",
    internal_trimming=False,
    charsets=False,
    assembler="trinity",
)
