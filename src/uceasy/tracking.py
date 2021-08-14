r"""Provenance tracking module.

This CSV file stores information about how UCEasy was run,
such as system information and parameters used.
"""

import csv
import sys
import platform
import getpass


from uceasy.adapters import CommandResult


tracking = {
    "UCEasy command": sys.argv,
    "Standard output": None,
    "Execution time": None,
    "Who ran": getpass.getuser(),
    "Operating System": platform.platform(),
    "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
}


def save_tracking_file(cmds: List[CommandResult]):
    first_row = []
    second_row = []
    cmds_rows = []
    for k, v in tracking.items():
        first_row.append(k)
        second_row.append(v)

    for cmd in cmds:
        row = []
        row[0] = cmd.command
        row[1] = cmd.stdout
        row[2] = cmd.execution_time
        row[3] = "UCEasy"
        cmds_rows.append(row)

    with open(path, "w") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(first_row)
        writer.writerow(second_row)
        for c in cmds_rows:
            writer.writerow(c)
