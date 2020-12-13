#!/bin/bash


export PYTHONPATH="$PWD/GetSmells:/Applications/Understand.app/Contents/MacOS/Python"

echo $PWD

python3 -W ignore ./GetSmells/src/main.py
