import configparser
import csv
from typing import List


def load_csv(path: str, delimiter: str = ",") -> List[str]:
    """Read the csv file content and return a list of rows."""
    with open(path, "r") as f:
        reader = csv.reader(f, delimiter=delimiter)

        # Ignore header
        next(reader)

        return [row for row in reader]


def dump_config_file(
    path: str, config: dict, allow_no_value: bool = False
) -> None:
    """Read a dictionary and create a .ini style configuration file."""
    config = configparser.ConfigParser(
        delimiters=(":"), allow_no_value=allow_no_value
    )
    config.optionxform = str
    config.read_dict(config)

    with open(path, "w") as fl:
        config.write(fl, space_around_delimiters=False)
