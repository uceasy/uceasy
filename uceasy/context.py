from collections import namedtuple


params = (
        'input',
        'output',
        'sheet',
        'adapter_i5',
        'adapter_i7',
        'probes',
        'assembler',

        # OPTIONAL
        'fastq_encoding',
        'min_len',
        'r1_pattern',
        'r2_pattern',
        'no_merge',
        'single_end'
        )

defaults = (
        None,
        None,
        None,
        None,
        None,
        None
        )

Context = namedtuple('Context', params, defaults=defaults)

