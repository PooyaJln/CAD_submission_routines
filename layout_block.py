import os
import pyautocad
import codecs
import pathlib
# from pyautocad import Autocad


def cad_actions(file):
    #    with open (file, 'w') as f:
    f = open(file, 'wb')
    acad = pyautocad.Autocad()
    for doc in acad.app.Documents:
        print(doc.Name)
        print(doc.Layouts.Count)
        # more actions
    f.close()


given_path = input("Please enter your directory:")
given_folder = pathlib.Path(given_path)
for dirpath, dirnames, filenames in (os.walk(given_path)):
    for filename in filenames:
        if filename.lower().endswith('.dwg'):
            file_to_funct = given_folder / filename
            cad_actions(file_to_funct)
