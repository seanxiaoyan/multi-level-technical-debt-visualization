#!/bin/bash

if [[ "$OSTYPE" == "darwin"* ]]; then
export PYTHONPATH="$PWD/GetSmells:/Applications/Understand.app/Contents/MacOS/Python"
fi


py -W ignore ./GetSmells/src/main.py
