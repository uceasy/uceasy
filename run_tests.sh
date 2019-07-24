#!/bin/sh


if [ ! -e testdata/output/ ]; then
	mkdir testdata/output
else
	rm -r testdata/output/*
fi


echo "Running tests..."

pytest tests/
