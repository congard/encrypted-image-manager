#!/usr/bin/env python3

from config import *
from shutil import rmtree

import os
import subprocess


def rmfile(file):
    if file is not None:
        if os.path.exists(file):
            os.remove(file)


# we need to disable systemd service
subprocess.call(['systemctl', 'disable', os.path.basename(unmounterServiceInstallPath), '--now'])
subprocess.call(['systemctl', 'daemon-reload'])

rmtree(installDir)
rmfile(iconInstallPath)
rmfile(desktopInstallPath)
rmfile(unmounterServiceInstallPath)
