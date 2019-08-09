#!/bin/sh


if [ ! -e testoutput/ ]; then
	mkdir testoutput
else
	rm -r testoutput/*
fi


echo "Running tests..."

pytest tests/
