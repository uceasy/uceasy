<p>
    <img src="docs/img/uceasy_logo.png" height="200px">

</p>

[![Tests](https://github.com/uceasy/uceasy/workflows/Tests/badge.svg)](https://github.com/uceasy/uceasy/actions?workflow=Tests)
[![codecov](https://codecov.io/gh/uceasy/uceasy/branch/master/graph/badge.svg)](https://codecov.io/gh/uceasy/uceasy)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=uceasy_uceasy&metric=alert_status)](https://sonarcloud.io/dashboard?id=uceasy_uceasy)
[![DOI](https://zenodo.org/badge/203415455.svg)](https://zenodo.org/badge/latestdoi/203415455)

# UCEasy: a software package based on good practices in scientific computing for phylogenetic analysis of UCEs


__UCEasy__ is a wrapper to automate manual procedures of the [PHYLUCE](https://phyluce.readthedocs.io/en/latest) software package by abstracting the pipeline steps into 3 major commands and choosing sensible defaults for its command-line options, easing the execution and improving reproducibility.


At the moment, the only software package for analysing [ultraconserved elements](https://www.ultraconserved.org/) (UCEs) is PHYLUCE, but its execution can be quite challenging especially for non-computer experts.
__UCEasy__ is a convenient tool that automates the execution of common tasks for most types of UCE analysis, these being Quality Control, Assembly and UCE Processing.

For more information check out our [Wiki](https://github.com/uceasy/uceasy/wiki).
## Installation Guide
### Dependencies
* Python ^3.7
* PHYLUCE 1.6.*

See [releases](https://github.com/uceasy/uceasy/releases) for pre-built binaries for Linux. Or install it from [PyPI](https://pypi.org/project/uceasy/):
```
$ pip install uceasy
```
Then, make sure you have a working installation of PHYLUCE, check out the installation guide at [PHYLUCE's documentation](https://phyluce.readthedocs.io/en/latest/installation.html).


## Workflow
The operations [Quality Control](https://github.com/uceasy/uceasy/wiki/QualityControl), [Assembly](https://github.com/uceasy/uceasy/wiki/Assembly) and [Phylogenomics](https://github.com/uceasy/uceasy/wiki/Phylogenomics) represent the following workflow.

<p>
    <img src="docs/img/workflow.png" height="500px">

</p>

The colored boxes are UCEasy CLI commands.
```
$ uceasy quality-control
$ uceasy assembly
$ uceasy phylogenomics
```
Explore the options for these commands with the `--help` flag.<br>
For a guide of how to use UCEasy see: [Tutorial](https://github.com/uceasy/uceasy/wiki/Tutorial).


## Acknowledgements

We thank the following institutions, which contributed to ensuring the success of our work:

Ministério da Ciência, Tecnologia, Inovação e Comunicação (MCTIC)

Museu Paraense Emílio Goeldi (MPEG)

Instituto Nacional de Pesquisas da Amazônia (INPA)

Centro Universitário do Estado do Pará (CESUPA)

## Funding

 This research was supported  by Conselho Nacional de Desenvolvimento Científico e Tecnológico - CNPq (fellowships 149985/2018-5; 129954/2018-7).

## Authors

 Caio Vinícius Raposo Ribeiro<br>
 Lucas Peres Oliveira<br>
 Romina Batista<br>
 Marcos Paulo Alves de Sousa


 ## Contact

Dr. Marcos Paulo Alves de Sousa (Project leader)

_Email: **msousa@museu-goeldi.br**_<br>
_Laboratório de Biologia Molecular-LBM_<br>
_Grupo de pesquisa em Bioinformática e Informática para Biodiversidade (BioInfo)_<br>
_Museu Paraense Emílio Goeldi_<br>
_Av. Perimetral 1901. CEP 66077- 530. Belém, Pará, Brazil._
