
# OH Project (ArkTS) Commands on Linux

[English Version](README_en.md)



## 背景

由于一些比较可惜的原因，HUAWEI 官方对于 DevEco Studio 的支持仅限于 Windows 和 MacOS，在 Linux 上很难编译上传一个 ArkTS 项目。

于是本项目就计划着手解决这个问题，从**源码编译、镜像烧录（rk3568）到 ArkTS 项目上传**的全过程动作放到 Linux 平台，以提升开发的便捷性。



## 如何使用

### 前置条件

1. 将本项目 clone / 下载解压后，将项目根目录加入 `$PATH` 环境变量（建议写入 `.bashrc/.zshrc`）；
2. 准备 Java（1.8 以上）、Python3（3.6 以上），确保能在命令行调用 `java` 和 `python3`；



### 管理一个 ArkTS 项目

1. 准备 OpenHarmony SDK；
2. 设置环境变量 `OHOS_SDK`（建议写入 `.bashrc/.zshrc`）为你的 OpenHarmony SDK 的根目录。请注意，它需要包含 API 版本号，例如 `[...]/11`；
3. 在一个 **<u>OH ArkTS 项目的 根目录</u>** 下调用脚本即可！例如 `oh-sync-project`；
4. 对于一个新的 ArkTS 项目，需要先执行一次 `oh-sync-project`；

> 指令如下：
>
> - `oh-sync-project`：同步当前 ArkTS 项目；
> - `oh-sign-hap`：为当前 ArkTS 项目的 hap 包签名；
> - `oh-build-hap`：仅构建 ArkTS 项目为 hap 包；
> - `oh-install-hap`：仅安装 ArkTS 项目的输出 hap 包到开发板；
> - `oh-build-and-run`：构建 hap、签名并在开发板上运行项目；



### 烧录一个镜像

> 注意：采用 `upgrade_tool` 烧录工具，当前仅适用于 rk3568；

1. 将本项目根目录下 `etc/udev/rules.d/*` 复制到 `/etc/udev/rules.d/` 中，然后执行 `reload-udev.sh`，确保 Linux 能识别这个硬件；
2. 连接好开发板后，使用 `oh-flash <imageDir>` 烧录，期间注意留意提示信息。其中 `imageDir` 是存放镜像的目录，这个目录通常有 `config.cfg / parameter.txt` 等文件；



## 注意事项（必读）

- 由于 SDK API 的频繁变动，不保证代码兼容性。经过测试，本项目适用于 API 11、API 12 两个版本的 OpenHarmony SDK；

- 在 `$OHOS_SDK` 上层目录（即不包含 API 版本号的 SDK 根目录）下，必须要有 `licenses/`（官网下载 public SDK 时会附带），否则官方不允许使用 SDK，如下图所示：

  <img src="pictures/licenses.png" />

  > 如果你没有，可以将仓库里的 `licenses` 目录复制过去。

- 新的 ArkTS 项目第一次编译时会询问 `key-alias`（作为 hap 签名的键名），填一个唯一的（和其他项目不同的）只含字母和数字的值就行，其他直接回车默认。



