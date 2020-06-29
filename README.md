<p>
    <img src="docs/img/uceasy_logo.jpg" height="200px">

</p>

[![Tests](https://github.com/uceasy/uceasy/workflows/Tests/badge.svg)](https://github.com/uceasy/uceasy/actions?workflow=Tests)
[![codecov](https://codecov.io/gh/uceasy/uceasy/branch/master/graph/badge.svg)](https://codecov.io/gh/uceasy/uceasy)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=uceasy_uceasy&metric=alert_status)](https://sonarcloud.io/dashboard?id=uceasy_uceasy)

# UCEasy: a wrapper for the PHYLUCE software package


__UCEasy__ is a wrapper to automate manual procedures of the [PHYLUCE](https://phyluce.readthedocs.io/en/latest) software package by abstracting the pipeline steps in only one command, easing the execution and improving reproducibility.


At the moment, the only software for _in silico_ analysis of [ultraconserved elements](https://www.ultraconserved.org/) (UCEs) is Phyluce, but its execution can be quite challenging especially for non-computer experts.
__UCEasy__ is a convenient tool that automates the execution of common tasks for all types of UCE analysis, these being [Quality Control](https://phyluce.readthedocs.io/en/latest/quality-control.html), [Assembly](https://phyluce.readthedocs.io/en/latest/assembly.html) and [UCE Processing](https://phyluce.readthedocs.io/en/latest/uce-processing.html).

## Installation Guide
### Dependencies
* Python ^3.7
* PHYLUCE ^1.6

See [releases](https://github.com/uceasy/uceasy/releases) for pre-built binaries for Linux (statically linked against [musl libc](https://musl.libc.org/)). Or install it from [PyPI](https://pypi.org/project/uceasy/):
```
$ pip install uceasy
```
Then, make sure you have a working installation of PHYLUCE, check out the installation guide at [PHYLUCE's documentation](https://phyluce.readthedocs.io/en/latest/installation.html).


## Workflow
The operations [Quality Control](https://github.com/uceasy/uceasy/wiki/Quality-Control), [Assembly](https://github.com/uceasy/uceasy/wiki/Assembly) and [Phylogenomics](https://github.com/uceasy/uceasy/wiki/Phylogenomics) represent the following workflow.

<p>
    <img src="docs/img/workflow.png" height="500px">

</p>

The colored boxes are UCEasy CLI commands.
```
$ uceasy quality-control
$ uceasy assembly
$ uceasy phylogenomics
```
Explore the options for theses commands with the `--help` flag.<br>
For a guide of how to use UCEasy see: [Tutorial](https://github.com/uceasy/uceasy/wiki/Tutorial).


## Acknowledgements

We thank the following institutions, which contributed to ensuring the success of our work:

Ministério da Ciência, Tecnologia, Inovação e Comunicação (MCTIC)

Museu Paraense Emílio Goeldi (MPEG)

Instituto Nacional de Pesquisas da Amazônia (INPA)

Centro Universitário do Estado do Pará (CESUPA)

## Funding

This work has been supported by Conselho Nacional de Desenvolvimento Científico e Tecnológico - CNPq (grants 149985/2018-5; 129954/2018-7).

## Authors

 Marcos Paulo Alves de Sousa<br>
 Caio Vinícius Raposo Ribeiro <br>
 Lucas Peres Oliveira <br>
 Romina do Socorro da Silva Batista

 ## Contact

Dr. Marcos Paulo Alves de Sousa (Project leader)

_Email: **msousa@museu-goeldi.br**_<br>
_Laboratório de Biologia Molecular_<br>
_Museu Paraense Emílio Goeldi_<br>
_Av. Perimetral 1901. CEP 66077- 530. Belém, Pará, Brazil._
