from pytest_mock import mocker
import pytest
import os

from uceasy.controller.phyluce_facade import Facade
from uceasy.adapters import quality_control, assembly
from uceasy.controller import env_manager
from uceasy.use_cases.uce_phylogenomics import UCEPhylogenomics


OUTPUT = os.getcwd() + '/testoutput'


@pytest.fixture()
def facade():
    return Facade()


def test_quality_control(facade, mocker):
    input = 'testdata/raw_fastq'
    config_file = os.getcwd() + '/sample/output/illumiprocessor.conf'
    adapter_i7 = 'AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC*ATCTCGTATGCCGTCTTCTGCTTG'
    adapter_i5 = 'AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT'
    sheet = 'testdata/sample_sheet.csv'

    mocker.patch.object(env_manager, 'prepare_illumiprocessor_conf')
    mocker.patch.object(quality_control, 'run_illumiprocessor')

    mocked_render_conf_file = mocker.patch.object(env_manager, 'render_conf_file')
    mocked_render_conf_file.return_value = config_file

    facade.quality_control(input, OUTPUT, sheet, adapter_i7, adapter_i5)

    env_manager.prepare_illumiprocessor_conf.assert_called_once_with(sheet, adapter_i7, adapter_i5)
    env_manager.render_conf_file.assert_called_once()
    quality_control.run_illumiprocessor.assert_called_once_with(input, OUTPUT + '/clean_fastq', config_file)


def test_assembly(facade, mocker):
    assembler = 'trinity'
    samples = ['sample0']
    config_file = OUTPUT + '/assembly.conf'

    mocker.patch.object(env_manager, 'prepare_assembly_conf')
    mocker.patch.object(assembly, 'run_trinity')
    mocker.patch.object(assembly, 'run_spades')

    mocked_os_listdir = mocker.patch.object(os, 'listdir')
    mocked_os_listdir.return_value = samples
    mocked_render_conf_file = mocker.patch.object(env_manager, 'render_conf_file')
    mocked_render_conf_file.return_value = config_file

    facade.assembly(OUTPUT, assembler)

    env_manager.prepare_assembly_conf.assert_called_once_with(OUTPUT, samples)
    env_manager.render_conf_file.assert_called_once()
    assembly.run_trinity.assert_called_once_with(config_file, OUTPUT + '/assembly')


def test_process_uce(facade, mocker):
    contigs = OUTPUT + 'assembly/contigs'
    probes = 'testdata/probes.fasta'
    log = OUTPUT
    taxon_group = 'all'
    taxa = '1'
    aligner = 'mafft'
    charsets = False
    percent = '0.75'
    internal_trimming = True

    mocker.patch.object(UCEPhylogenomics, 'run_uce_processing')

    facade.process_uce(OUTPUT, log, contigs, probes, taxon_group, taxa, aligner, charsets, percent, internal_trimming)

    UCEPhylogenomics.run_uce_processing.assert_called_once()
