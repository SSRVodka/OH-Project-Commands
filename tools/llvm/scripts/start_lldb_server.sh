#!/system/bin/sh
# Copyright Huawei Technologies Co., Ltd. 2023-2023. All rights reserved.

umask 0027

LLDB_PATH=$1
LISTENER_SCHEME=$2
DEVICE=$3
WEB_SOCKET=$4
GDB_SOCKET_DIR=$5
LOG_CHANNELS=$6
PARAM_LIST=$@

i=1
for a in $PARAM_LIST
do
    if [ $i -gt 6 ]; then
        LOG_CHANNELS="$LOG_CHANNELS $a"
    fi
    i=$((i+1))
done

BIN_PATH=$LLDB_PATH/bin
LOG_PATH=$LLDB_PATH/log
TMP_PATH=$LLDB_PATH/tmp
LOG_FILE=$LOG_PATH/platform.log

export LLDB_DEBUGSERVER_LOG_FILE=$LOG_PATH/gdb-server.log
export LLDB_SERVER_LOG_CHANNELS="$LOG_CHANNELS"
export LLDB_DEBUGSERVER_DEVICE=$DEVICE
export LLDB_DEBUGSERVER_DOMAINSOCKET_DIR="$GDB_SOCKET_DIR"

chmod 0750 "$LLDB_PATH"
rm -r $TMP_PATH
mkdir $TMP_PATH
export TMPDIR=$TMP_PATH
rm -r $LOG_PATH
mkdir $LOG_PATH

cat </dev/null >"$LLDB_DEBUGSERVER_LOG_FILE" 2>"$LOG_FILE"

cd $TMP_PATH
$BIN_PATH/lldb-server platform --listen $LISTENER_SCHEME://$DEVICE/$WEB_SOCKET --log-file "$LOG_FILE" --log-channels "$LOG_CHANNELS" </dev/null >$LOG_PATH/platform-stdout.log 2>&1
