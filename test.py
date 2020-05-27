import os
import subprocess
import pyautocad
import pathlib
from pyautocad import Autocad
import time
import signal

acad_path = r"C:\Program Files\Autodesk\AutoCAD 2019\acad.exe"
accore_path = r"C:\Program Files\Autodesk\AutoCAD 2019\accoreconsole.exe"
file_in = r"C:\Users\poja\OneDrive\Ritdef\V-50-15-01071.dwg"

acad = pyautocad.Autocad()
cad_start = subprocess.Popen(acad_path)
time.sleep(15)
process = subprocess.Popen(file_in, shell = True)
print(process.pid)
time.sleep(15)
os.killpg(os.getpgid(process.pid, signal.SIGTERM))