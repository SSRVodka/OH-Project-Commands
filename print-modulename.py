#!/bin/python3
# @author SJTU-XHW
# @file print-modulename.py

import sys
from oh_utils import get_module_name

# argv[1]: project root directory


if __name__ == '__main__':
    assert len(sys.argv) == 2, f"Invalid parameters: {str(sys.argv)}"
    print(get_module_name(sys.argv[1])[0])

