import os
import shutil

PATH = os.getcwd()

if not os.path.isdir('data'):
    os.mkdir('data')

shutil.rmtree('data')

assembly_conf = ['[samples]\n', f'sample0:{PATH}/sample/clean_fastq/sample0/split-adapter-quality-trimmed/\n']

with open(f'{PATH}/sample/assembly.conf', 'w') as fl:
    fl.writelines(assembly_conf)

