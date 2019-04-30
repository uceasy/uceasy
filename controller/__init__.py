import os
import shutil
from getpass import getuser


USER = getuser()

# Directories
WORKENV = f'/home/{USER}/.uceasy/'
TEMPLATES = WORKENV + 'templates/'
CLEAN_FASTQ = WORKENV + 'data/clean_fastq'
TRINITY_ASSEMBLIES = WORKENV + 'data/trinity_assemblies'


# TODO
# replace jinja2 by configparser
template_illumiprocessor = '''[adapters]
{% for adapter in adapters -%}
{{ adapter }}
{% endfor %}
[tag sequences]
{% for tag_sequence in tag_sequences -%}
{{ tag_sequence }}
{% endfor %}
[tag map]
{% for tag_map in tag_maps -%}
{{ tag_map }}
{% endfor %}
[names]
{% for name in names -%}
{{ name }}
{% endfor -%}
'''
template_assembly = '''[samples]
{% for sample in samples -%}
{{ sample }}
{% endfor %}
'''


def create_workenv():
    os.mkdir(WORKENV)
    os.mkdir(TEMPLATES)
    with open(TEMPLATES + 'illumiprocessor.txt', 'w') as fl:
        fl.write(template_illumiprocessor)
        fl.close()
    with open(TEMPLATES + 'assembly.txt', 'w') as fl:
        fl.write(template_assembly)
        fl.close()


if not os.path.isdir(WORKENV):
    create_workenv()
else:
    shutil.rmtree(WORKENV)
    create_workenv()
