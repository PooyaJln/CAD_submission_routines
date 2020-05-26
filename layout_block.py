import os
import subprocess
import pyautocad
import pathlib
from pyautocad import Autocad

acad_path = r"C:\Program Files\Autodesk\AutoCAD 2019\acad.exe"
accore_path = r"C:\Program Files\Autodesk\AutoCAD 2019\accoreconsole.exe"

def cad_actions(file):
    acad = pyautocad.Autocad()
    shell_process = subprocess.Popen(file, shell = True) 
    print(shell_process.pid)


    # for doc in acad.app.Documents:
    #     print(doc.Name)
    
def make_file_list1(): #returns a list of file in a directory
    given_path = input("Please enter your directory:")
    file_list = [(given_path +"\\"+ item) for item in os.listdir(given_path) if item.endswith(".dwg")]
    print(file_list)
    for item in file_list:
        cad_actions(item)

# def make_file_list2():
given_path = input("Please enter your directory:")
given_folder = pathlib.Path(given_path) #creates a <class 'pathlib.WindowsPath'>
given_folder2= os.fspath(given_folder) #creates a string. so it's not necessary
print(given_path,"", type(given_path))
print(given_folder,"", type(given_folder))
print(given_folder2,"", type(given_folder2))
# for dirpath, dirnames, filenames in (os.walk(given_path)):
#     for filename in filenames:
#         if filename.lower().endswith('.dwg'):
#             file_to_funct = given_folder / filename
#             cad_actions(file_to_funct)
#             # print (file_to_funct)

