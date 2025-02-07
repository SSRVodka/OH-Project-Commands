#!/bin/python3
# @author SJTU-XHW
# @file print-abilityname.py

import sys
from oh_utils import get_ability_name, get_module_name

# argv[1]: project root directory


if __name__ == '__main__':
    assert len(sys.argv) == 3, f"Invalid parameters: {str(sys.argv)}"
    project_root = sys.argv[1]
    print(get_ability_name(project_root, get_module_name(project_root)[0])[0])



