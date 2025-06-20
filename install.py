#!/bin/python3
# @author SJTU-XHW
# @file install.py

# This script will help you install the tools on your machine!

### import test
import json5
### this is necessary for this project

import argparse
import sys
import os
import requests
import shutil
from zipfile import ZipFile
from pathlib import Path

repo_root_dir = os.path.dirname(__file__)
oh_cli_tool_dir = os.path.join(repo_root_dir, "tools")


def check_oh_cli_tool_exist() -> bool:
    return os.path.exists(os.path.join(oh_cli_tool_dir, "bin/hvigorw"))


def download_oh_cli_tools():
    url = "https://github.com/SSRVodka/fs/releases/download/v0.0.0/commandline-tools-linux-x64-5.0.9.310.zip"
    tmp_file = "tmp"
    extracted_dir = "command-line-tools"
    target_dir = "tools"

    try:
        print(f"[INFO] Downloading {url} ...")
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(tmp_file, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print("[INFO] Finish downloading.")

        print("[INFO] Unzipping tools...")
        with ZipFile(tmp_file, 'r') as zip_ref:
            zip_ref.extractall()
        print("[INFO] Finish unzipping.")

        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)

        os.rename(extracted_dir, target_dir)
        print(f"[INFO] move {extracted_dir} to {target_dir}")

    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        # 清理临时文件
        if os.path.exists(tmp_file):
            os.remove(tmp_file)
            print("[INFO] temporary files are cleaned")


def main():
    parser = argparse.ArgumentParser(description="install script parameters")
    parser.add_argument("--override", action="store_true", help="override old versions")
    args = parser.parse_args()

    if args.override or not check_oh_cli_tool_exist():
        download_oh_cli_tools()
    
    os.makedirs(os.path.join(repo_root_dir, "oh-sign-certs/repo"), exist_ok=True)

    print("[INFO] Installation finished. Remember to set $OHOS_SDK in your .bashrc/.zshrc. See README.md")
    print("[INFO] 安装完成。接下来请继续阅读 README 文档，它将引导您把 $OHOS_SDK 环境变量设置于您的 .bashrc/.zshrc 中，以便后续使用。")


if __name__ == "__main__":
    main()
