from multiprocessing import cpu_count
import json
import subprocess
import os


# Get environment variable UCEASY_PHYLUCE, default: phyluce
phyluce_env = os.getenv('UCEASY_PHYLUCE', 'phyluce')

# Search for phyluce environment and loads a json string
cmd = ['conda', 'search', '--envs', '--json', phyluce_env]
out = subprocess.check_output(cmd)
phyluce_json = json.loads(out)

if not phyluce_json[0]['location']:
    raise IOError('Phyluce was not found, specify the conda environment with the UCEASY_PHYLUCE variable.')

PHYLUCE         = phyluce_json[0]['location']
TRIMMOMATIC     = PHYLUCE + '/bin/trimmomatic'
ILLUMIPROCESSOR = PHYLUCE + '/bin/illumiprocessor'
SCRIPT_TRINITY  = PHYLUCE + '/bin/phyluce_assembly_assemblo_trinity'

CPU = str(cpu_count() - 2)
