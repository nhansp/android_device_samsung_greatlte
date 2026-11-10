#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)

# Camera
$(call soong_config_set,samsungCameraVars,extra_ids,20)

# Overlays
PRODUCT_PACKAGES += \
    FrameworkResOverlayGreatlte

# Common tree
$(call inherit-product, device/samsung/universal8895-common/common.mk)

# Proprietary files
$(call inherit-product, vendor/samsung/greatlte/greatlte-vendor.mk)
