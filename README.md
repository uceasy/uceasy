<p>
    <img src="doc/img/UCEasy_logo.jpg" height="200px">
</p>

# UCEasy: wrapper for the Phyluce software package

__UCEasy__ is a wrapper to automate manual procedures of the [Phyluce](https://phyluce.readthedocs.io/en/latest) software package by abstracting the pipeline steps in only one command, easing the execution and improving reproducibility.


At the moment, the only software for _in silico_ analysis of [ultraconserved elements](https://www.ultraconserved.org/) (UCEs) is Phyluce, but its execution can be quite challenging especially for non-computer experts.
__UCEasy__ is a convenient tool that automates the execution of common tasks for all types of UCE analysis, these being [Quality Control](https://phyluce.readthedocs.io/en/latest/quality-control.html), [Assembly](https://phyluce.readthedocs.io/en/latest/assembly.html) and [UCE Processing](https://phyluce.readthedocs.io/en/latest/uce-processing.html).

<p align="center">
    <img src="doc/img/phyluce_diagram.png">
</p>

We also designed it with _Clean Architecture_ principes in mind, the follow image shows the software architecture of UCEasy.

<p align="center">
    <img src="doc/img/uceasy_architecture.png" height="500px">
</p>
    
## Pros
* Automation of the pipeline steps
* Easier to execute
* Extensible software architecture


## Installation Guide
### Dependencies
* Python 3.7
* Python's official package installer (pip)
* Conda (with bioconda channel  set up)

### Installing UCEasy
UCEasy is available at PyPI, so can be easily installed with pip.
```
pip install uceasy
```
__Obs: Make sure you are installing with the system's Python 3.7 and not conda's, otherwise they won't work together as Phyluce is written in Python 2.7.__

### Setting up Phyluce
To use Phyluce you need to install it from the bioconda channel, see instructions of how to install conda and set bioconda channels at (https://bioconda.github.io/user/install.html).

Create a conda environment for Phyluce and activate it with to following commands.
```
conda create -n phyluce
conda activate phyluce
```
Next, install Phyluce.
```
conda install phyluce
```
At this point you should be able to use UCEasy together with Phyluce, we'll explain how to do that in the next session.

## Usage
### _TODO_
