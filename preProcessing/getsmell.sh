#!/bin/bash


export PYTHONPATH="$PWD/GetSmells:/Applications/Understand.app/Contents/MacOS/Python"


python3 -W ignore ./GetSmells/src/main.py
