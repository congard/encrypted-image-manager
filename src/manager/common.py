import re
import subprocess


def getLoopDevice(image, devices):
    result = re.search(
        r'(/dev/loop[0-9]+)[ \t]+(?:[0-9]+[ \t]+){4}(?:' + image + r')[ \t]+(?:[0-9]+[ \t]*){2}',
        str(devices))

    if result is None:
        return None
    else:
        return result.group(1)


def getLoopDevices():
    process = subprocess.Popen(["losetup"], stdout=subprocess.PIPE)
    return process.communicate()
