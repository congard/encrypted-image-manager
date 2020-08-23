#!/usr/bin/env python3

from config import images
from common import *

mountProcess = subprocess.Popen(['mount'], stdout=subprocess.PIPE)
mountDevices = mountProcess.communicate()

for img in images:
    mapperPoint = images[img]['mapper-point']
    mapperPath = '/dev/mapper/' + mapperPoint

    if re.search(mapperPath, str(mountDevices)) is not None:
        subprocess.call(['umount', mapperPath])
        subprocess.call(['cryptsetup', 'luksClose', mapperPoint])
        subprocess.call(['losetup', '-d', getLoopDevice(img, getLoopDevices())])
