from collections import namedtuple


params = (
    "input",
    "output",
    "sheet",
    "adapter_i7",
    "adapter_i5",
    "probes",
    "assembler",
    "aligner",
    "charsets",
    "percent",
    "internal_trimming",
    # OPTIONAL
    "fastq_encoding",
    "min_len",
    "r1_pattern",
    "r2_pattern",
    "no_merge",
    "single_end",
)

defaults = (None, None, None, None, None, None)

Context = namedtuple("Context", params, defaults=defaults)
