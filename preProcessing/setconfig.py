#!/usr/bin/python
import configparser
import os
import sys
import subprocess
from pathlib import Path

#set config.ini
file_path = os.path.realpath(__file__)
dir_path = os.path.dirname(file_path)
root_path = Path(dir_path).parent

proj_path = sys.argv[1]
proj_name = proj_path.split('/')[-1]

parser = configparser.ConfigParser()
config_path = os.path.join(root_path,'GetSmells/config.ini')
parser.read(config_path)

parser.remove_section('main.projPaths')

parser.add_section('main.projPaths')
parser.set('main.projPaths', proj_name, proj_path)
with open(config_path, 'w') as configfile:
    parser.write(configfile)