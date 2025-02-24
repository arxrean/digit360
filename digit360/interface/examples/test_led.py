# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import cv2
import sys
import pdb
sys.path.append("/home/zkou/Code/digit360")
from digit360.interface.control.led import led_all_off, led_set_channel
from digit360.interface.digit360 import Digit360
from digit360.interface.usb.usb import get_digit360_devices
import proto as d360frame

# get sorted device list connected when multiple digit360 connected
connected_devices = get_digit360_devices()

# Takes first device
descriptor = connected_devices[0]

led_all_off(Digit360(descriptor.data))
led_set_channel(Digit360(descriptor.data), d360frame.LightingChannel.CHANNEL_1, (255, 0, 0))
led_set_channel(Digit360(descriptor.data), d360frame.LightingChannel.CHANNEL_2, (0, 255, 0))
led_set_channel(Digit360(descriptor.data), d360frame.LightingChannel.CHANNEL_3, (0, 0, 255))
# led_set_channel(Digit360(descriptor.data), d360frame.LightingChannel.CHANNEL_4, (255, 0, 0))
# led_set_channel(Digit360(descriptor.data), d360frame.LightingChannel.CHANNEL_5, (0, 255, 0))
# led_set_channel(Digit360(descriptor.data), d360frame.LightingChannel.CHANNEL_6, (0, 0, 255))
# led_set_channel(Digit360(descriptor.data), d360frame.LightingChannel.CHANNEL_7, (255, 0, 0))
# led_set_channel(Digit360(descriptor.data), d360frame.LightingChannel.CHANNEL_8, (0, 255, 0))
