# Encrypted image mounter

<img src="src/installer/icon.svg" width="256" height="256">

<small>Icon taken from <a href=https://www.flaticon.com/free-icon/data-encryption_1813806>flaticon.com</a></small>

The scripts that automatically mounts/unmounts your encrypted image(s).

## Setup
1. Create image if not created yet:
   ```bash
   dd if=/dev/zero of=documents.img bs=2G count=4
   losetup -f documents.img
   losetup # extract X from this comand
   cryptsetup luksFormat -v /dev/loopX
   cryptsetup luksOpen /dev/loopX mapperPoint
   mkfs.ext4 /dev/mapper/mapperPoint
   ```
   will create 8GiB image file. You need to do this only once for storage creation
   
2. `cd src/manager`

3. Edit `images.py` (file contains example)

4. If you want to use `desktop` file without asking your sudo password, you should create next record in `/etc/sudoers`:
   ```conf
   <username> ALL=(root) NOPASSWD: </path/to/installed/mounter.py>
   ```

## Installation
1. `cd src/installer`

2. Edit `config.py` if you need. You can mark the unnecessary files as `None`

3. Execute:
   ```bash
   chmod +x installer.py
   sudo ./installer.py
   ```
   or
   ```bash
   sudo python3 installer.py
   ```
   
You can uninstall scripts by executing `uninstaller.py`

## Usage
Double click on the `desktop` file and type your password. Encrypted file will be automatically mounted.
<br>If you didn't mark `unmounterServiceInstallPath` as `None`, then your encrypted image(s) will be automatically
unmounted before the shutdown
