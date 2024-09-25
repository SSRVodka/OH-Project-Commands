#!/bin/python3
# @author SJTU-XHW
# @file print-bundlename.py

import sys
import os
import json

# argv[1]: project root directory

assert len(sys.argv) == 2, f"Invalid parameters: {str(sys.argv)}"

with open(os.path.join(f"{sys.argv[1]}", "AppScope/app.json5"), "r") as app_conf:
    app_conf_data = json.load(app_conf)

print(app_conf_data["app"]["bundleName"])


