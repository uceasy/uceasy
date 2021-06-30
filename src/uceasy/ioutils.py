import configparser
import csv
import os
import shutil
import logging
from typing import List, Dict, Optional
from types import SimpleNamespace


from uceasy import __version__


def generate_log(path: str):
    uname = os.uname()
    logging.basicConfig(
        format="%(asctime)s %(levelname)s: %(message)s",
        filename=f"{path}/uceasy.log",
        level=logging.INFO
    )
    logging.info(f"Starting UCEasy v{__version__}")
    logging.info(f"System name: {uname.sysname}")
    logging.info(f"Node name: {uname.nodename}")
    logging.info(f"Release: {uname.release}")
    logging.info(f"Version: {uname.version}")
    logging.info(f"Machine: {uname.machine}")


def print_cli_flags_to_log(namespace: SimpleNamespace):
    for k, v in namespace.__dict__.items():
        logging.info(f"{k}: {v}")


def load_csv(path: str, delimiter: str = ",") -> List[List[str]]:
    """Read the csv file content and return a list of rows."""
    with open(path, "r") as f:
        reader = csv.reader(f, delimiter=delimiter)

        # Ignore header
        next(reader)

        return [row for row in reader]


def dump_config_file(path: str, config: Dict[str, Dict[str, Optional[str]]]) -> None:
    """Read a dictionary and create a .ini style configuration file."""
    parser = configparser.ConfigParser(delimiters=(":"), allow_no_value=True)
    parser.optionxform = str  # type: ignore
    parser.read_dict(config)

    with open(path, "w") as fl:
        parser.write(fl, space_around_delimiters=False)


def get_taxa_from_contigs(contigs: str) -> int:
    """Return the taxa number from the contigs directory."""
    return len([name for name in os.listdir(contigs)])


def delete_output_dir_if_exists(output: str):
    """Use this if you want the underlining tool to create the output dir for you,
    without being interrupted by its own overwrite prompt."""
    if os.path.exists(output):
        answer = input(f"Output directory exists. Overwrite {output}/ [Y/n]? ")
        if answer not in "Yy ":
            exit()
        else:
            shutil.rmtree(output)


def create_output_dir(output: str):
    delete_output_dir_if_exists(output)
    os.makedirs(output)
