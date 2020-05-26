import os
import subprocess
import pyautocad
import pathlib
from pyautocad import Autocad

acad_path = r"C:\Program Files\Autodesk\AutoCAD 2019\acad.exe"
accore_path = r"C:\Program Files\Autodesk\AutoCAD 2019\accoreconsole.exe"

def cad_actions(file_in):
    acad = pyautocad.Autocad()
    shell_process = subprocess.Popen(file_in, shell = True) 
    print(shell_process.pid)


    # for doc in acad.app.Documents:
    #     print(doc.Name)
    
def file_list_by_file_name(): #returns a list of file in a directory
    file_list = []
    file_path = input("please enter the address to the file and when you are done enter ""done!"" ")
    while file_path != "done".lower():
        if file_path.endswith(".dwg"):
            file_list.append(file_path)
            file_path = input ("Please add your next file")
    print(file_list)
    


def file_list_by_dir():
    given_path = input("Please enter your directory:")
    given_folder = pathlib.Path(given_path) #creates a <class 'pathlib.WindowsPath'>
    file_list =  [entry.path for entry in os.scandir(given_path) if entry.name.endswith(".dwg")]
    print (file_list)

file_list_by_file_name()
#given_folder2= os.fspath(given_folder) #creates a string. so it's not necessary
#print(given_path,"", type(given_path))
#print(given_folder,"", type(given_folder))
#print(given_folder2,"", type(given_folder2))
#print(tuple(os.walk(given_folder)))



