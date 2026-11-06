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
        .add_needed('libcompiler_rt.so'),
    'vendor/lib/libhifistill.so': blob_fixup()
        .add_needed('libprocessgroup.so'),
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
    'vendor/lib/libexynoscamera.so': blob_fixup()
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
