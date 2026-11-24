#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Boot image: the stock DTBH entry covers board revisions 6 to 255
BOARD_DTBH_HW_REV := 6
BOARD_DTBH_HW_REV_END := 255

include device/samsung/universal8895-common/BoardConfigCommon.mk

DEVICE_PATH := device/samsung/greatlte

# Display
TARGET_SCREEN_DENSITY := 420

# Kernel
TARGET_KERNEL_CONFIG += vendor/greatlte.config
TARGET_KERNEL_DTB := vendor/samsung/exynos8895-greatlte.dtb
TARGET_DTB_LIST_WILDCARD := vendor/samsung/exynos8895-greatlte

# Proprietary files
include vendor/samsung/greatlte/BoardConfigVendor.mk
