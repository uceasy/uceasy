import click
import os

from . import __version__
from .operations import parse_illumiprocessor_config, parse_assembly_config
from .adapters import ADAPTERS
from .ioutils import load_csv, dump_config_file


@click.group()
@click.version_option(version=__version__)
def cli():
    """A unified CLI for the PHYLUCE software package."""
    pass


@cli.command()
@click.argument("raw-fastq", required=True)
@click.option(
    "--csv",
    required=True,
    help="CSV table containing the adapters and barcode information. (see the docs to learn how to create your csv file).",
)
@click.option(
    "--cores",
    "-j",
    type=int,
    required=True,
    help="Number of computer cores to use",
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
    help="Output directory for the clean fastq reads. (default: current directory)",
)
@click.option(
    "--r1-pattern",
    "--r1",
    help="An optional regex pattern to find R1 reads. (default: None)",
)
@click.option(
    "--r2-pattern",
    "--r2",
    help="An optional regex pattern to find R2 reads. (default: None)",
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
    raw_fastq,
    csv,
    cores,
    single_end,
    single_index,
    r1_pattern,
    r2_pattern,
    phred64,
    output,
    min_len,
    no_merge,
):
    """Runs quality control with illumiprocessor."""

    if output is None:
        output = os.getcwd()

    if not os.path.exists(output):
        os.makedirs(output)

    # Create and save the configuration file
    config_output = f"{output}/illumiprocessor.conf"
    csv_file = load_csv(csv)
    config = parse_illumiprocessor_config(csv_file)
    dump_config_file(config_output, config)

    cmd = f"--input {raw_fastq} --output {output}/clean-fastq --cores {cores} --config {config_output}".split()

    # 40 is the default in illumiprocessor
    if min_len != 40:
        cmd.extend(["--min-len", min_len])
    if r1_pattern:
        cmd.extend(["--r1-pattern", r1_pattern])
    if r2_pattern:
        cmd.extend(["--r2-pattern", r2_pattern])
    if phred64:
        cmd.extend("--phred", "phred64")
    if single_end:
        cmd.append("--se")
    if no_merge:
        cmd.append("--no-merge")

    ADAPTERS["illumiprocessor"](cmd)


@cli.command()
def assembly():
    pass


@cli.command()
def uce_processing():
    pass
