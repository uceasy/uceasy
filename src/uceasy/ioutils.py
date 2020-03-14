import configparser
import csv


def load_csv(path, delimiter=","):
    with open(path, "r") as f:
        reader = csv.reader(f, delimiter=delimiter)

        # Ignore header
        next(reader)

        return [row for row in reader]


def dump_config_file(file, config_dict, allow_no_value=False):
    config = configparser.ConfigParser(delimiters=(":"), allow_no_value=allow_no_value)
    config.optionxform = str
    config.read_dict(config_dict)

    with open(file, "w") as fl:
        config.write(fl, space_around_delimiters=False)
