from multiprocessing import cpu_count
import json
import subprocess
import os


# Get environment variable UCEASY_PHYLUCE, default: phyluce
phyluce_env = os.getenv('UCEASY_PHYLUCE', 'phyluce')

# Search for phyluce using conda's search feature
# if found, returns a json string.
args = ['conda', 'search', '--envs', '--json', phyluce_env]
cmd = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = cmd.communicate()
phyluce_json = json.loads(out)
if not phyluce_json:
    raise IOError('The phyluce path was not found, please check your phyluce installation\n' +
                  'You can specify which conda environment phyluce is installed with the' +
                  'environment variable UCEASY_PHYLUCE.')

# Programs
PHYLUCE = phyluce_json[0]['location']
TRIMMOMATIC = PHYLUCE + '/bin/trimmomatic'
ILLUMIPROCESSOR = PHYLUCE + '/bin/illumiprocessor'
SCRIPT_TRINITY = PHYLUCE + '/bin/phyluce_assembly_assemblo_trinity'
CPU = str(cpu_count() - 2)
