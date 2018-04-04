import smb
from smb.SMBConnection import SMBConnection
import shutil
from ..Config import ConfigHandler
import platform

prefs = ConfigHandler.get_property_list();
smb_conn = SMBConnection(prefs['smbusername'], prefs['smbpassword'], platform.node())
smb_conn.connect(prefs['smbip'])

def move_file(path, target):
    shutil.move(path, target)

def move_folder(path, target):
    shutil.move(path, target)
