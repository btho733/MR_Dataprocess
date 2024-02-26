# This file selects only the T2vWeighted MR volumes corresponding to baseline visits ( Visits 1 and 2)
# from a large dataset containing multiple MR aquisitions and saves the renamed copy for further analysis
import SimpleITK as sitk
import numpy as np
%matplotlib notebook
import matplotlib.pyplot as plt
import gui
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

import os
import nibabel as nb
'''
    For the given path, get the List of all files in the directory tree 
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles        
def main():
    
    dirName = '/Users/PathTo/RootFolder'
    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)
    numfiles=0
    numextracted =0
    # Print the files
    for elem in listOfFiles:
        if elem.endswith("T2W.nii.gz"):
            print('Reading', elem)
            patientnum = elem[58:62]
            visitnum = int(elem[71])
            if visitnum ==1 or visitnum ==2:
              newelem = f"{dirName}/../Files_extracted/{patientnum}_v{str(visitnum)}_T2W.nii.gz"
              os.rename(elem,newelem)
              numextracted+=1
            else:
                print("File not from visit 1 or 2 !")
            numfiles+=1
            print('Copying.....')
    print(numextracted, 'files extracted')   
        
if __name__ == '__main__':
    main()
