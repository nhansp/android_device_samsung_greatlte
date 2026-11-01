#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/non_ab_device.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/product_launched_with_n_mr1.mk)

$(call inherit-product, device/samsung/greatlte/device.mk)

TARGET_SCREEN_HEIGHT := 2960
TARGET_SCREEN_WIDTH := 1440

$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_NAME := lineage_greatlte
PRODUCT_DEVICE := greatlte
PRODUCT_BRAND := samsung
PRODUCT_MODEL := SM-N950N
PRODUCT_MANUFACTURER := samsung

PRODUCT_GMS_CLIENTID_BASE := android-samsung

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="greatlteks-user 9 PPR1.180610.011 N950NKSU5DZE2 release-keys" \
    BuildFingerprint=samsung/greatlteks/greatlteks:9/PPR1.180610.011/N950NKSU5DZE2:user/release-keys \
    DeviceProduct=greatlteks
