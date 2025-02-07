#!/bin/python3
# @author SJTU-XHW
# @file oh-config-profile-template.py

import sys
import json
from oh_utils import get_bundle_name, get_module_name, get_module_permissions

# argv[1]: project root directory
# argv[2]: template JSON file
project_root = sys.argv[1]
template_src = sys.argv[2]
bundle_name = get_bundle_name(project_root)
module_name = get_module_name(project_root)[0]

assert len(sys.argv) == 3, f"Invalid parameters: {str(sys.argv)}"

with open(template_src, "r") as profile_template:
    template_data = json.load(profile_template)

# Replace bundle name
template_data["bundle-info"]["bundle-name"] = bundle_name
# Append system permissions
template_data["acls"]["allowed-acls"] = get_module_permissions(project_root, module_name)

with open(template_src, "w") as profile_template:
    json.dump(template_data, profile_template, indent=4)
