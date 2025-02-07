#!/bin/python3
# @author SJTU-XHW
# @file print-bundlename.py

import sys
from oh_utils import get_bundle_name

# argv[1]: project root directory


if __name__ == '__main__':
    assert len(sys.argv) == 2, f"Invalid parameters: {str(sys.argv)}"
    print(get_bundle_name(sys.argv[1]))
