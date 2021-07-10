r"""Provenance tracking module.

This CSV file stores information about how UCEasy was run,
such as system information and parameters used.
"""

import csv
import platform
from datetime import datetime
from types import SimpleNamespace


def save_tracking_file(path: str, context: SimpleNamespace):
    first_row = ["Operating System", "Current Time"]
    second_row = [platform.platform(), datetime.now()]
    for k, v in context.__dict__.items():
        first_row.append(k)
        second_row.append(v)

    with open(path, "w") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(first_row)
        writer.writerow(second_row)
