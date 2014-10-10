# Vim YouCompleteMe completion configuration for Android ART development.
# To use, copy in <aosp>/art/.ycm_extra_conf.py. See
# https://github.com/Valloric/YouCompleteMe.
#
# License: This file is placed in the public domain.

import os
import platform

repo_root = os.path.dirname(os.path.abspath(__file__))

# Paths in the compilation flags must be absolute to allow ycm to find them from
# any working directory.
def AbsolutePath(path):
  return os.path.join(repo_root, path)

flags = [
  '-I', AbsolutePath('../external/libcxx/include'),
  '-I', AbsolutePath('../art/disassembler'),
  '-I', AbsolutePath('../external/gtest/include'),
  '-I', AbsolutePath('../external/valgrind/main/include'),
  '-I', AbsolutePath('../external/valgrind/main'),
  '-I', AbsolutePath('../external/vixl/src'),
  '-I', AbsolutePath('../external/vixl/src/a64'),
  '-I', AbsolutePath('../external/zlib'),
  '-I', AbsolutePath('../frameworks/compile/mclinker/include'),
  '-I', AbsolutePath('../art/runtime'),
  '-I', AbsolutePath('../art/compiler'),
  '-I', AbsolutePath('../out/target/product/generic_arm64/obj/SHARED_LIBRARIES/libartd-compiler_intermediates'),
  '-I', AbsolutePath('../out/target/product/generic_arm64/gen/SHARED_LIBRARIES/libartd-compiler_intermediates'),
  '-I', AbsolutePath('../libnativehelper/include/nativehelper'),
  '-isystem', AbsolutePath('../system/core/include'),
  '-isystem', AbsolutePath('../hardware/libhardware/include'),
  '-isystem', AbsolutePath('../hardware/libhardware_legacy/include'),
  '-isystem', AbsolutePath('../hardware/ril/include'),
  '-isystem', AbsolutePath('../libnativehelper/include'),
  '-isystem', AbsolutePath('../frameworks/native/include'),
  '-isystem', AbsolutePath('../frameworks/native/opengl/include'),
  '-isystem', AbsolutePath('../frameworks/av/include'),
  '-isystem', AbsolutePath('../frameworks/base/include'),
  '-isystem', AbsolutePath('../external/skia/include'),
  '-isystem', AbsolutePath('../out/target/product/generic_arm64/obj/include'),
  '-isystem', AbsolutePath('../bionic/libc/arch-arm64/include'),
  '-isystem', AbsolutePath('../bionic/libc/include'),
  '-isystem', AbsolutePath('../bionic/libstdc++/include'),
  '-isystem', AbsolutePath('../bionic/libc/kernel/uapi'),
  '-isystem', AbsolutePath('../bionic/libc/kernel/uapi/asm-arm64'),
  '-isystem', AbsolutePath('../bionic/libm/include'),
  '-isystem', AbsolutePath('../bionic/libm/include/arm64'),
  '-include', AbsolutePath('../build/core/combo/include/arch/linux-arm64/AndroidConfig.h'),
  '-I', AbsolutePath('../build/core/combo/include/arch/linux-arm64/'),

  '-Wwrite-strings',
  '-std=c++11',
  '-DNDEBUG',
  '-x','c++'
]

if platform.machine() !='aarch64':
  flags.append('-DUSE_SIMULATOR')


def FlagsForFile(filename, **kwargs):
  return {
    'flags': flags,
    'do_cache': True
  }

