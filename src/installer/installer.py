#!/usr/bin/env python3

from config import *

import os
import subprocess


def getContent(path):
    f = open(path, "r")
    content = f.read()
    f.close()
    return content


def writeContent(content, path):
    f = open(path, 'w')
    f.write(content)
    f.close()


def join(p1, p2):
    if p1 is None or p2 is None:
        return None

    return os.path.join(p1, p2)


# for files located in src/manager directory
def mgr(p):
    return '../manager/' + p


files = {
    mgr('mounter.py'): {
        'install': join(installDir, 'mounter.py'),
        'cp': True
    },
    mgr('unmounter.py'): {
        'install': join(installDir, 'unmounter.py'),
        'cp': True
    },
    mgr('config.py'): {
        'install': join(installDir, 'config.py'),
        'cp': True
    },
    mgr('common.py'): {
        'install': join(installDir, 'common.py'),
        'cp': True
    },
    'Encrypted Image Mounter.desktop': {
        'install': desktopInstallPath,
        'cp': False
    },
    'icon.svg': {
        'install': iconInstallPath,
        'cp': True
    },
    'encrypted-image-unmounter.service': {
        'install': unmounterServiceInstallPath,
        'cp': False
    }
}

# create dirs if does not exists
for file in files:
    install = files[file]['install']

    if install is None:
        continue

    directory = os.path.dirname(install)

    if not os.path.exists(directory):
        os.makedirs(directory)

# generate & install desktop file
if desktopInstallPath is not None:
    desktop = getContent("Encrypted Image Mounter.desktop")
    desktop = desktop.format(path=files[mgr('mounter.py')]['install'], iconPath=iconInstallPath)

    writeContent(desktop, desktopInstallPath)

# generate & install service file
if unmounterServiceInstallPath is not None:
    service = getContent('encrypted-image-unmounter.service')
    service = service.format(unmounterPath=files[mgr('unmounter.py')]['install'])

    writeContent(service, unmounterServiceInstallPath)

# install other files by copying
for file in files:
    fileInfo = files[file]
    install = fileInfo['install']

    if install is None:
        continue

    if fileInfo['cp'] is True:
        subprocess.call(['cp', file, install])

# we need to enable & start systemd service
if unmounterServiceInstallPath is not None:
    subprocess.call(['systemctl', 'daemon-reload'])
    subprocess.call(['systemctl', 'enable', os.path.basename(unmounterServiceInstallPath), '--now'])

print("Installation done")
