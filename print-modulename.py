#!/bin/python3
# @author SJTU-XHW
# @file print-modulename.py

import sys
import json

# argv[1]: project root directory

assert len(sys.argv) == 2, f"Invalid parameters: {str(sys.argv)}"

with open(f"{sys.argv[1]}/build-profile.json5", "r") as app_conf:
    app_conf_data = json.load(app_conf)

modules = app_conf_data["modules"]
for mod in modules:
    print(mod["name"])



