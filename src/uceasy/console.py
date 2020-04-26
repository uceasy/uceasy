import click
import os
from typing import Optional

from . import __version__
from .facade import AssemblyFacade, QualityControlFacade, UCEPhylogenomicsFacade


THREADS = os.cpu_count()


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(version=__version__)
def cli():
    """A unified CLI for the PHYLUCE software package."""
    pass


@cli.command()
@click.argument("raw-fastq", required=True)
@click.argument("csv-file", required=True)
@click.option(
    "--threads",
    "-j",
    type=int,
    default=THREADS,
    help="Number of computer threads to use. (default: all available)",
)
@click.option(
    "--min-len",
    "-m",
    type=int,
    default=40,
    help="The minimum length of reads to keep. (default: 40)",
)
@click.option(
    "--output",
    "-o",
    default=os.getcwd(),
    help="Output directory. (default: current directory)",
)
@click.option(
    "--r1-pattern", "--r1", help="An optional regex pattern to find R1 reads.",
)
@click.option(
    "--r2-pattern", "--r2", help="An optional regex pattern to find R2 reads.",
)
@click.option(
    "--phred64",
    "-p",
    is_flag=True,
    help="Use phred64 for fastq encoding. (default: phred33)",
)
@click.option("--single-end", "--se", is_flag=True, help="Single-end reads.")
@click.option(
    "--single-index", "--si", is_flag=True, help="Single-indexed for barcodes."
)
@click.option(
    "--no-merge",
    "-n",
    is_flag=True,
    help="When trimming PE reads, do not merge singleton files.",
)
def quality_control(
    raw_fastq: str,
    csv_file: str,
    threads: int,
    single_end: bool,
    single_index: bool,
    r1_pattern: Optional[str],
    r2_pattern: Optional[str],
    phred64: bool,
    output: str,
    min_len: int,
    no_merge: bool,
) -> None:
    """Run quality control with illumiprocessor."""
    facade = QualityControlFacade(
        raw_fastq,
        csv_file,
        threads,
        single_end,
        single_index,
        r1_pattern,
        r2_pattern,
        phred64,
        output,
        min_len,
        no_merge,
    )
    facade.run()


@cli.command()
@click.argument("clean-fastq", required=True)
@click.option(
    "--config",
    "-c",
    type=str,
    help="Custom configuration file containing the reads to assemble.",
)
@click.option(
    "--kmer", "-k", type=str, help="The kmer value to use.",
)
@click.option(
    "--threads",
    "-j",
    type=int,
    default=THREADS,
    help="Number of computer threads to use. (default: all available)",
)
@click.option(
    "--output",
    "-o",
    type=str,
    default=os.getcwd(),
    help="Output directory. (default: current directory)",
)
@click.option(
    "--no-clean", "-n", is_flag=True, help="Do not clean intermediate files.",
)
@click.option(
    "--subfolder",
    "-s",
    type=str,
    help="A subdirectory, below the level of the group, containing the reads.",
)
def assembly(
    clean_fastq: str,
    threads: int,
    output: str,
    config: Optional[str],
    kmer: Optional[str],
    no_clean: bool,
    subfolder: Optional[str],
) -> None:
    """Run assembly with spades."""
    facade = AssemblyFacade(
        clean_fastq, threads, output, config, kmer, no_clean, subfolder,
    )
    facade.run()


@cli.command()
@click.argument("contigs", required=True)
@click.argument("probes", required=True)
@click.option(
    "--aligner",
    "-a",
    type=str,
    default="mafft",
    help="Aligner program to use.",
)
@click.option(
    "--charsets", "-c", is_flag=True, help="Use charsets.",
)
@click.option(
    "--threads",
    "-j",
    type=int,
    default=THREADS,
    help="Number of computer threads to use. (default: all available)",
)
@click.option(
    "--output",
    "-o",
    type=str,
    default=os.getcwd(),
    help="Output directory. (default: current directory)",
)
@click.option(
    "--internal-trimming",
    "-i",
    is_flag=True,
    help="Internally trim the alignments.",
)
@click.option(
    "--log-dir",
    "-l",
    type=str,
    default=os.getcwd(),
    help="Directory to save logs.",
)
@click.option(
    "--percent", "-p", type=float, required=True, help="The kmer value to use.",
)
def phylogenomics(
    aligner: str,
    charsets: bool,
    contigs: str,
    internal_trimming: bool,
    output: str,
    log_dir: str,
    probes: str,
    percent: float,
    threads: int,
):
    facade = UCEPhylogenomicsFacade(
        aligner,
        charsets,
        contigs,
        internal_trimming,
        output,
        log_dir,
        probes,
        percent,
        threads,
    )
    facade.run()
