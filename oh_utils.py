#!/bin/python3
# @author SJTU-XHW
# @file oh_utils.py

import os
import json5
import re
from typing import List


def remove_comments(json5_str: str) -> str:
    """
    Remove the comments in JSON 5 format files
    """
    # Remove single-line comments
    json5_str = re.sub(r'//.*', '', json5_str)
    # Remove multi-line comments
    json5_str = re.sub(r'/\*.*?\*/', '', json5_str, flags=re.DOTALL)
    return json5_str


def get_ability_name(project_root: str, module_name: str) -> List[str]:
    with open(os.path.join(f"{project_root}", f"{module_name}/src/main/module.json5"), "r") as module_conf:
        json5_str = module_conf.read()
        # json_str = remove_comments(json5_str)
        # module_conf_data = json.loads(json_str)
        module_conf_data = json5.loads(json5_str)
        return [ability["name"] for ability in module_conf_data["module"]["abilities"]]


def get_bundle_name(project_root: str) -> str:
    with open(os.path.join(f"{project_root}", "AppScope/app.json5"), "r") as app_conf:
        json5_str = app_conf.read()
        # json_str = remove_comments(json5_str)
        # app_conf_data = json.loads(json_str)
        app_conf_data = json5.loads(json5_str)
        return app_conf_data["app"]["bundleName"]


def get_module_name(project_root: str) -> List[str]:
    with open(f"{project_root}/build-profile.json5", "r") as app_conf:
        json5_str = app_conf.read()
        # json_str = remove_comments(json5_str)
        # app_conf_data = json.loads(json_str)
        app_conf_data = json5.loads(json5_str)
        return [mod["name"] for mod in app_conf_data["modules"]]


def get_module_permissions(project_root: str, module_name: str) -> List[str]:
    with open(os.path.join(f"{project_root}", f"{module_name}/src/main/module.json5"), "r") as module_conf:
        json5_str = module_conf.read()
        # json_str = remove_comments(json5_str)
        # module_conf_data = json.loads(json_str)
        module_conf_data = json5.loads(json5_str)
        module_root = module_conf_data["module"]
        if module_root.get("requestPermissions") is None:
            return []
        requested_perms = module_root["requestPermissions"]
        return [perm["name"] for perm in requested_perms]

