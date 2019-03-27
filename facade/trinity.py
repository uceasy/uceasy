import subprocess
import os
from jinja2 import Environment, FileSystemLoader
from facade import WORKENV, SAMPLE_NAMES, CLEAN_FASTQ, CPU


# Trinity arguments
OUTPUT = WORKENV + 'data/trinity-assemblies'
CONF = WORKENV + 'assembly.conf'


def run_assembly():
    samples = prepare_samples_for_conf_file(SAMPLE_NAMES, CLEAN_FASTQ)
    conf_generated = _render_conf_file(samples)
    if not conf_generated:
        raise IOError('assembly.conf was not generated')
    cmd = [
        'phyluce_assembly_assemblo_trinity',
        '--conf', CONF,
        '--output', OUTPUT,
        '--clean',
        '--cores', CPU
    ]
    return subprocess.run(cmd, check=True)


def _render_conf_file(samples):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('assembly.txt')

    with open(CONF, 'w') as conf_file:
        settings = template.render(samples=samples)

        conf_file.write(settings)

    return os.path.isFile(CONF)


def prepare_samples_for_conf_file(SAMPLE_NAMES, CLEAN_FASTQ):
    samples = []
    for sample in SAMPLE_NAMES:
        samples.append(f'{sample}:{CLEAN_FASTQ}/{sample}/split-adapter-quality-trimmed/')

    return samples
