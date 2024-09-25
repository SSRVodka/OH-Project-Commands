#!/bin/python3
# @author SJTU-XHW
# @file oh-flash.py

import os
import sys

proc_excluded = ["uboot"]

def proc_gpt(gpt: str, tool: str, img_dir: str) -> None:
    print("Flashing loader...")
    os.system("%s UL %s -noreset" % (tool, os.path.join(img_dir, "MiniLoaderAll.bin")))
    print("Flashing GPT parameters...")
    os.system("%s DI -p %s" % (tool, os.path.join(img_dir, "parameters.txt")))
    print("Flashing uboot...")
    os.system("%s DI -uboot %s %s" % (tool, os.path.join(img_dir, "uboot.img"), os.path.join(img_dir, "parameters.txt")))

    gpt = gpt.strip()
    entries = gpt.split(',')
    for entry in entries:
        addr_start = entry.find('@') + 1
        addr_end = entry.find('(')
        name_start = addr_end + 1
        name_end = entry.find(':')
        if name_end == -1:
            name_end = len(entry) - 1
        name = entry[name_start:name_end].replace('-', '_')
        addr = entry[addr_start:addr_end]
        if name in proc_excluded:
            continue
        print("Flashing %s to LBA %s" % (name, addr))
        if not os.path.exists(os.path.join(img_dir, "%s.img" % name)):
            print("Skipped %s" % name)
        else:
            os.system("%s WL %s %s.img" % (tool, addr, os.path.join(img_dir, name)))


if __name__ == '__main__':

    base_dir = os.path.dirname(sys.argv[0])

    _tool = os.path.join(base_dir, "bin/flash.%s" % os.uname().machine)

    if len(sys.argv) < 2:
        print("Usage: %s <imageDir>" % os.path.basename(sys.argv[0]).split('.')[0])
        exit(255)

    _img_dir = sys.argv[1]
    if not os.path.isfile(os.path.join(_img_dir, "parameter.txt")):
        print("Not a valid image directory: %s" % _img_dir)
        exit(1)

    os.system('%s LD' % _tool)

    ans = input("Continue to flash? (Y/n) ")
    if not ans == "Y":
        print("Abort.")
        sys.exit(0)

    with open(os.path.join(_img_dir, "parameter.txt"), "r") as params:
        for line in params:
            if line.find('CMDLINE') == -1:
                continue
            raw = line.split('=')[1]
            start_idx = raw.find(':')
            gpt = raw[start_idx+1:]
            proc_gpt(gpt, _tool, _img_dir)

    ans = input("Restart now? (Y/n) ")
    if ans == "Y":
        os.system("%s RD" % _tool)

