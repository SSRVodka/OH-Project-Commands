
if [ -z $OHOS_SDK ]; then
echo "Please set OHOS_SDK first!"
else
export CC=${OHOS_SDK}/native/llvm/bin/clang
export CXX="${OHOS_SDK}/native/llvm/bin/clang++"
export AS=${OHOS_SDK}/native/llvm/bin/llvm-as
export LD=${OHOS_SDK}/native/llvm/bin/ld.lld
export LDXX=${LD}
export LLD=${LD}
export STRIP=${OHOS_SDK}/native/llvm/bin/llvm-strip
export RANLIB=${OHOS_SDK}/native/llvm/bin/llvm-ranlib
export OBJDUMP=${OHOS_SDK}/native/llvm/bin/llvm-objdump
export OBJCOPY=${OHOS_SDK}/native/llvm/bin/llvm-objcopy
export READELF=${OHOS_SDK}/native/llvm/bin/llvm-readelf
export NM=${OHOS_SDK}/native/llvm/bin/llvm-nm
export AR=${OHOS_SDK}/native/llvm/bin/llvm-ar
export PROFDATA=${OHOS_SDK}/native/llvm/bin/llvm-profdata
export CFLAGS="--target=aarch64-linux-ohos -fPIC -D__MUSL__=1"
export CXXFLAGS="--target=aarch64-linux-ohos -fPIC -D__MUSL__=1"
export LDFLAGS="-fuse-ld=lld --target=aarch64-linux-ohos"

export PATH=$PATH:${OHOS_SDK}/native/llvm/bin:${OHOS_SDK}/native/toolchains
fi
