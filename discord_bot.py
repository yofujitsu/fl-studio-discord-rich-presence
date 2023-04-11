import subprocess
import pyautogui
from pypresence import Presence
from time import time

def process_exists():
    progs = str(subprocess.check_output('tasklist'))
    if ("FL64.exe" or "FL32.exe") in progs:
        return True
    else:
        return False

def project_name():
    windows = pyautogui.getAllWindows()
    fl = ''
    for window in windows:
        if window.title == "FL Studio 20":
            fl = "untitled.flp"
        elif "FL Studio 20" in window.title:
            fl = window.title
            x = len(fl)
            fl = fl[:len(fl)-15]
    return fl

RPC = Presence("1095311176658862151")
RPC.connect()
while(True):
    if(process_exists()):
        RPC.update(
            details=project_name(),
            start=time(),
            large_image="logo",
            large_text="Making music"
        )
    else:
        print("waiting for launch")