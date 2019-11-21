from multiprocessing import cpu_count
import json
import subprocess
import os


# Get environment variable UCEASY_PHYLUCE, default: phyluce
phyluce_env = os.getenv("UCEASY_PHYLUCE", "phyluce")
cmd = ["conda", "search", "--envs", "--json", phyluce_env]
out = subprocess.check_output(cmd)
phyluce_json = json.loads(out)


try:
    PHYLUCE = phyluce_json[0]["location"]
except IndexError:
    raise IOError(
        "Phyluce was not found, specify the conda environment with the UCEASY_PHYLUCE variable."
    )


TRIMMOMATIC = PHYLUCE + "/bin/trimmomatic"
ILLUMIPROCESSOR = PHYLUCE + "/bin/illumiprocessor"
TRINITY = PHYLUCE + "/bin/phyluce_assembly_assemblo_trinity"
SPADES = PHYLUCE + "/bin/phyluce_assembly_assemblo_spades"

CPU = str(cpu_count() - 2)
