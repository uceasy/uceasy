#!/bin/sh


SAMPLE_URL="https://ndownloader.figshare.com/articles/1284521/versions/1"


if [ -e testdata/raw_fastq/ ]; then
	echo "Found sample in testdata."
else
	echo "Sample not found, downloading..."
	wget -O testdata/raw_fastq.zip $SAMPLE_URL
	unzip testdata/raw_fastq -o testdata/
	rm testdata/raw_fastq.zip
fi


if [ ! -e testdata/output/ ]; then
	mkdir testdata/output
else
	rm -r testdata/output/*
fi


echo "Running tests..."

pytest tests/
