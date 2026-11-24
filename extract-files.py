#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/samsung/universal8895-common',
    'hardware/samsung',
    'vendor/samsung/universal8895-common',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    (
        'vendor/lib/libOpenCv.camera.samsung.so',
        'vendor/lib/libxcv.camera.samsung.so',
    ): blob_fixup()
        .add_needed('libcompiler_rt-samsung.so')
        .add_needed('libshim_aeabi.so'),
    'vendor/lib/libhifistill.so': blob_fixup()
        .add_needed('libprocessgroup.so')
        .add_needed('libshim_cxa_demangle.so'),
    'vendor/lib/libhifistill_tuning.so': blob_fixup()
        .fix_soname(),
    'vendor/lib/libsmartfocusengine.so': blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    (
        'vendor/lib/hw/camera.universal8895.so',
        'vendor/lib/libexynoscamera3.so',
    ): blob_fixup()
        .replace_needed('libcamera_client.so', 'libcamera_compat.so')
        .replace_needed('libgui.so', 'libgui_vendor.so'),
    'vendor/lib/libexynoscamera3.so': blob_fixup()
        .binary_regex_replace(b'system.camera.CC.disable', b'vendor.camera.CC.disable')
        .binary_regex_replace(b'_ZN7android5FenceC1Ei', b'_ZN7libui285FenceC1Ei')
        .binary_regex_replace(b'_ZN7android5Fence4waitEi', b'_ZN7libui285Fence4waitEi')
        .add_needed('libshim_fence.so')
        # IMX333/2L2 preview size count 26 -> 27
        .sig_replace(
            '41 f2 30 37 40 f8 07 c0 41 f2 38 37 c4 51 ',
            '00f59857bc631b243c6300bf00bf')
        # 27-entry size list with 3840x2160 added; configureStreams validates video sizes against it
        .sig_replace(
            '00 0f 00 00 70 08 00 00 00 00 00 00 c0 0c 00 00 2c 07 00 00 00 00 00 00 00 0a 00 00 a0 05 00 00 '
            '00 00 00 00 b0 08 00 00 38 04 00 00 08 00 00 00 40 06 00 00 b0 04 00 00 01 00 00 00 00 05 00 00 '
            'c0 03 00 00 01 00 00 00 20 04 00 00 60 03 00 00 06 00 00 00 c0 03 00 00 c0 03 00 00 02 00 00 00 '
            'c0 03 00 00 1c 02 00 00 00 00 00 00 80 02 00 00 68 01 00 00 00 00 00 00 10 02 00 00 b0 01 00 00 '
            '06 00 00 00 20 03 00 00 58 02 00 00 01 00 00 00 20 03 00 00 e0 01 00 00 05 00 00 00 a0 02 00 00 '
            'c0 01 00 00 03 00 00 00 e0 01 00 00 40 01 00 00 03 00 00 00 e0 01 00 00 0e 01 00 00 00 00 00 00 '
            '20 10 00 00 18 0c 00 00 01 00 00 00 20 10 00 00 12 09 00 00 00 00 00 00 00 10 00 00 00 0c 00 00 '
            '01 00 00 00 00 10 00 00 00 09 00 00 00 00 00 00 00 0f 00 00 70 08 00 00 00 00 00 00 80 0c 00 00 '
            '60 09 00 00 01 00 00 00 00 0c 00 00 c0 06 00 00 00 00 00 00 ac 0b 00 00 ac 0b 00 00 02 00 00 00 '
            '60 0a 00 00 d6 05 00 00 00 00 00 00 20 0a 00 00 98 07 00 00 01 00 00 00 20 0a 00 00 90 07 00 00 '
            '01 00 00 00 00 0a 00 00 80 07 00 00 01 00 00 00 90 09 00 00 90 09 00 00 02 00 00 00 00 08 00 00 '
            '00 06 00 00 01 00 00 00 a0 05 00 00 38 04 00 00 01 00 00 00 38 04 00 00 38 04 00 00 02 00 00 00 '
            '50 06 00 00 38 04 00 00 03 00 00 00 d0 04 00 00 f0 03 00 00 06 00 00 00 20 04 00 00 c0 02 00 00 '
            '03 00 00 00 d0 02 00 00 d0 02 00 00 02 00 00 00 60 01 00 00 20 01 00 00 06 00 00 00 f8 01 00 00 '
            '78 01 00 00 01 00 00 00 78 01 00 00 78 01 00 00 02 00 00 00 f0 01 00 00 18 01 00 00 00 00 00 00 '
            '00 00 00 00 00 00 00 00 02 00 00 00 80 07 00 00 38 04 00 00 00 00 00 00 a0 05 00 00 a0 05 00 00 '
            '02 00 00 00 a0 05 00 00 38 04 00 00 01 00 00 00 40 04 00 00 40 04 00 00 02 00 00 00 00 05 00 00 '
            'd0 02 00 00 00 00 00 00 c0 03 00 00 d0 02 00 00 01 00 00 00 20 03 00 00 c2 01 00 00 00 00 00 00 '
            'd0 02 00 00 e0 01 00 00 03 00 00 00 80 02 00 00 e0 01 00 00 01 00 00 00 e0 01 00 00 40 01 00 00 '
            '03 00 00 00 60 01 00 00 20 01 00 00 06 00 00 00 40 01 00 00 f0 00 00 00 01 00 00 00 00 01 00 00 '
            '90 00 00 00 00 00 00 00 b0 00 00 00 90 00 00 00 06 00 00 00 00 0f 00 00 70 08 00 00 00 00 00 00 ',
            'c00f0000d00b000001000000c00f0000dc08000000000000000f00007008000000000000d00b0000d00b000002000000900f0000ac0b000001000000c00c00009009000001000000c00c00002c07000000000000a00b0000a00b000002000000400b00007008000001000000000a0000a005000000000000700800007008000002000000000800008004000000000000800700003804000000000000a0050000380400000100000040040000400400000200000000050000d00200000000000020040000c002000003000000000400000003000001000000c0030000d00200000100000020030000c201000000000000d0020000d002000002000000d0020000e00100000300000080020000e00100000100000060010000200100000600000040010000f000000001000000000100009000000000000000b00000009000000006')
        # point sensorInfo at the new list
        .sig_replace(
            '6c ce 09 00 34 ce 09 00 78 d0 09 00 ',
            '6cce09008cd0')
        # 16:9 preview row uses the 4032x2268 mode (60 fps) instead of 4032x3024
        .sig_replace(
            '00 00 00 00 c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 '
            'd0 0b 00 00 c0 0f 00 00 d0 0b 00 00 01 00 00 00 c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 d0 0b 00 00 '
            'c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 d0 0b 00 00 02 00 00 00 c0 0f 00 00 '
            'd0 0b 00 00 c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 '
            'd0 0b 00 00 03 00 00 00 c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 d0 0b 00 00 '
            'c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 d0 0b 00 00 04 00 00 00 c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 '
            'd0 0b 00 00 c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 d0 0b 00 00 05 00 00 00 '
            'c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 d0 0b 00 00 '
            'c0 0f 00 00 d0 0b 00 00 06 00 00 00 c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 '
            'd0 0b 00 00 c0 0f 00 00 d0 0b 00 00 c0 0f 00 00 d0 0b 00 00 07 00 00 00 ',
            '00000000c00f0000dc080000c00f0000dc080000c00f0000dc080000c00f0000dc080000c00f0000dc08'),
    'vendor/lib/libexynoscamera.so': blob_fixup()
        .binary_regex_replace(b'system.camera.CC.disable', b'vendor.camera.CC.disable')
        .replace_needed('libcamera_client.so', 'libcamera_compat.so')
        .replace_needed('libgui.so', 'libgui_vendor.so')
        .add_needed('libexynoscamera_shim.so')
        .remove_needed('libsec-ril.so')
        .remove_needed('libsecril-client.so'),
    'vendor/lib/libsensorlistener.so': blob_fixup()
        .replace_needed('libandroid.so', 'libsensorndkbridge.so'),
    'vendor/lib/libsnap_compute.so': blob_fixup()
        .replace_needed('libOpenCL.so', 'libGLES_mali.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'greatlte',
    'samsung',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(module, 'universal8895-common', module.vendor)
    utils.run()
