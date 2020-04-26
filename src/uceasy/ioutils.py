import configparser
import csv
import os
from typing import List, Dict, Optional


def load_csv(path: str, delimiter: str = ",") -> List[List[str]]:
    """Read the csv file content and return a list of rows."""
    with open(path, "r") as f:
        reader = csv.reader(f, delimiter=delimiter)

        # Ignore header
        next(reader)

        return [row for row in reader]


def dump_config_file(
    path: str,
    config: Dict[str, Dict[str, Optional[str]]],
    allow_no_value: bool = False,
) -> None:
    """Read a dictionary and create a .ini style configuration file."""
    parser = configparser.ConfigParser(
        delimiters=(":"), allow_no_value=allow_no_value
    )
    parser.optionxform = str  # type: ignore
    parser.read_dict(config)

    with open(path, "w") as fl:
        parser.write(fl, space_around_delimiters=False)


def get_taxa_from_contigs(contigs: str) -> int:
    """Return the taxa number from the contigs directory."""
    return len([name for name in os.listdir(contigs)])
