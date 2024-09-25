#!/bin/python3
# @author SJTU-XHW
# @file print-abilityname.py

import sys
import os
import json

# argv[1]: project root directory
# argv[2]: module name

assert len(sys.argv) == 3, f"Invalid parameters: {str(sys.argv)}"

with open(os.path.join(f"{sys.argv[1]}", f"{sys.argv[2]}/src/main/module.json5"), "r") as module_conf:
    module_conf_data = json.load(module_conf)

for ability in module_conf_data["module"]["abilities"]:
    print(ability["name"])



