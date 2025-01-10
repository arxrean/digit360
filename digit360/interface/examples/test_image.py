# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import cv2
import sys
sys.path.append("/home/zkou/Code/digit360")
import pdb
from digit360.interface.usb.usb import get_digit360_devices

# Example instantiation of Digit360Descriptor takes first device
descriptor = get_digit360_devices()[0]

dev = cv2.VideoCapture(descriptor.ics)

while True:
    ret, frame = dev.read()
    cv2.imshow('Digit 360', frame)
    mean_val = frame.reshape(-1, 3).mean(0)
    print("RGB mean values: ({:.4f}, {:.4f}, {:.4f})".format(mean_val[0], mean_val[1], mean_val[2]))
    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

dev.release()
cv2.destroyAllWindows()
