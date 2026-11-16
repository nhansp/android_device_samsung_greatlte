#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)

# Camera
# Camera 50 is the telephoto camera (stock cameradata/camera-feature.xml BACK_TELE_CAMERA_ID)
$(call soong_config_set,samsungCameraVars,extra_ids,50)

PRODUCT_PACKAGES += \
    ApertureOverlayGreatlte

# Overlays
PRODUCT_PACKAGES += \
    FrameworkResOverlayGreatlte

# Face unlock: the iris scanner, as stock greatlte ships it
UNIVERSAL8895_FACE_UNLOCK := iris

# Common tree
$(call inherit-product, device/samsung/universal8895-common/common.mk)

# Proprietary files
$(call inherit-product, vendor/samsung/greatlte/greatlte-vendor.mk)
