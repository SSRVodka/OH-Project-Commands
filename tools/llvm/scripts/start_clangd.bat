@rem Copyright (c) Huawei Technologies Co., Ltd. 2019-2020. All rights reserved.
@rem Description : clangd startup script
@echo off

set /A error_arg_count = 0
REM check if there are 6 arguments, more than 6 arguments will be ignored
IF %1.==. set /A error_arg_count+=1
IF %2.==. set /A error_arg_count+=1
IF %3.==. set /A error_arg_count+=1
IF %4.==. set /A error_arg_count+=1
IF %5.==. set /A error_arg_count+=1
IF %6.==. set /A error_arg_count+=1

if %error_arg_count% NEQ 0 (
	echo Usage:
	echo 	%0 [-CLANGD_PATH CLANGD_PATH] [-JSON_PATH JSON_PATH_DIR] [-CLANG_TIDY CLANG_TIDY]
	exit /b
)

REM Settle Parameters
:LOOP
	set index=%1
	if %index%! == ! goto END
	if "%index%"=="-CLANGD_PATH" (
		set CLANGD_PATH=%2
		shift
		)

	if "%index%"=="-JSON_PATH" (
		set JSON_PATH=%2
		shift
		)

    if "%index%"=="-CLANG_TIDY" (
		set CLANG_TIDY=%2
		shift
		)

	shift
	goto LOOP

:END

REM Settle CLANGD_PATH in front of PATH
set PATH=%CLANGD_PATH%;%PATH%

if [%CLANG_TIDY%] == [disable] (
   REM Run Clangd without clang-tidy
   echo disableClangTidy
   clangd -log=error --header-insertion=iwyu --background-index --suggest-missing-includes -compile-commands-dir=%JSON_PATH% --clang-tidy --clang-tidy-checks="-*"
) else (
   REM Run Clangd with clang-tidy and checks
   echo enableClangTidy
   clangd -log=error --header-insertion=iwyu --background-index --suggest-missing-includes -compile-commands-dir=%JSON_PATH% --clang-tidy
)
