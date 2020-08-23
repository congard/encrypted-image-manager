#!/usr/bin/env python3

from os import path

from config import images
from common import *

loopDevices = getLoopDevices()

for img in images:
    loopDevice = getLoopDevice(img, loopDevices)

    if loopDevice is None:
        subprocess.call(('losetup -f ' + img).split())
        loopDevices = getLoopDevices()
        loopDevice = getLoopDevice(img, loopDevices)

    mapperPoint = images[img]['mapper-point']
    mountPoint = images[img]['mount-point']
    mapperPath = '/dev/mapper/' + mapperPoint

    if not path.exists(mapperPath):
        try:
            subprocess.check_call(['cryptsetup', 'luksOpen', loopDevice, mapperPoint])
        except Exception as error:
            print("Notice: " + str(error))

    mountProcess = subprocess.Popen(['mount'], stdout=subprocess.PIPE)
    mountDevices = mountProcess.communicate()

    if re.search(mapperPath, str(mountDevices)) is None:
        subprocess.call(['mount', mapperPath, mountPoint])
