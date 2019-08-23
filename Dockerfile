FROM continuumio/miniconda2


# Use bash for the shell
SHELL ["bash", "-c"]


# Setup bioconda
RUN conda config --add channels defaults && \
  conda config --add channels bioconda && \
  conda config --add channels conda-forge


# Install phyluce
RUN conda install phyluce==1.6.7
