import click
import os
from typing import List, Optional

from . import __version__
from .operations import parse_illumiprocessor_config, parse_assembly_config
from .adapters import ADAPTERS
from .ioutils import load_csv, dump_config_file


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

    if not os.path.exists(output):
        os.makedirs(output)

    # Create and save the configuration file
    config_output = f"{output}/illumiprocessor.conf"
    csv = load_csv(csv_file)
    config = parse_illumiprocessor_config(csv)
    dump_config_file(config_output, config)

    cmd = (
        f"--input {raw_fastq} --output {output}/clean-fastq --cores {threads} "
        f"--config {config_output}"
    ).split()

    # 40 is the default in illumiprocessor
    if min_len != 40:
        cmd.extend(["--min-len", min_len])
    if r1_pattern:
        cmd.extend(["--r1-pattern", r1_pattern])
    if r2_pattern:
        cmd.extend(["--r2-pattern", r2_pattern])
    if phred64:
        cmd.extend(["--phred", "phred64"])
    if single_end:
        cmd.append("--se")
    if no_merge:
        cmd.append("--no-merge")

    ADAPTERS["illumiprocessor"](cmd)


@cli.command()
@click.argument("clean-fastq", required=True)
@click.option(
    "--assembler",
    "-a",
    type=str,
    default="spades",
    help="The assembler program to use. (default: spades)",
)
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
    assembler: str,
    config: Optional[str],
    kmer: Optional[str],
    no_clean: bool,
    subfolder: Optional[str],
) -> None:
    """Run assembly with spades or trinity."""
    if not os.path.exists(output):
        os.makedirs(output)

    # Create and save the configuration file
    if not config:
        config = f"{output}/assembly.conf"
        config_dict = parse_assembly_config(clean_fastq)
        dump_config_file(config, config_dict)

    cmd = (
        f"--output {output}/{assembler}-assemblies --cores {threads} "
        f"--config {config}"
    ).split()

    if assembler == "spades":
        if no_clean:
            cmd.append("--do-not-clean")
    else:
        if not no_clean:
            cmd.append("--clean")

    if kmer:
        if assembler == "trinity":
            cmd.extend(["--min-kmer-coverage", kmer])
        else:
            cmd.extend(["--kmer", kmer])
    if subfolder:
        cmd.extend(["--subfolder", subfolder])

    try:
        ADAPTERS[assembler](cmd)
    except KeyError:
        raise IOError(
            f"Could not find assembler: {assembler}.\n"
            "Make sure the assembler you chose is supported by UCEasy."
        )


@cli.command()
def uce_processing():
    pass
