#!/bin/python3
# @author SJTU-XHW
# @file oh-config-proj-sign.py
# argv[1]: "project directory",
# argv[2]: "certpath",
# argv[3]: "storePassword",
# argv[4]: "keyAlias",
# argv[5]: "keyPassword",
# argv[6]: "profile",
# argv[7]: "signAlg",
# argv[8] "storeFile"

import json
import os
import sys

assert len(sys.argv) == 9, f"Invalid parameters: {str(sys.argv)}"
build_conf_fn = os.path.join(f"{sys.argv[1]}", "build-profile.json5")

with open(build_conf_fn, "r") as build_conf:
    build_conf_data = json.load(build_conf)

build_conf_data["app"]["signingConfigs"] = [{
    "name": "default",
    "material": {
        "certpath": sys.argv[2],
        "storePassword": sys.argv[3],
        "keyAlias": sys.argv[4],
        "keyPassword": sys.argv[5],
        "profile": sys.argv[6],
        "signAlg": sys.argv[7],
        "storeFile": sys.argv[8]
    }
}]

with open(build_conf_fn, "w") as build_conf:
    json.dump(build_conf_data, build_conf, indent=4)
