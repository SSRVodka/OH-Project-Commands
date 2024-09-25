#!/bin/python3
# @author SJTU-XHW
# @file oh-config-profile-template.py

import sys
import json

# argv[1]: template JSON file
# argv[2]: bundle name

assert len(sys.argv) == 3, f"Invalid parameters: {str(sys.argv)}"

with open(sys.argv[1], "r") as profile_template:
    template_data = json.load(profile_template)

template_data["bundle-info"]["bundle-name"] = sys.argv[2]
with open(sys.argv[1], "w") as profile_template:
    json.dump(template_data, profile_template, indent=4)


