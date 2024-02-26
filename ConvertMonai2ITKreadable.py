# Converts Segmentation outputs from MONAI (One-hot encoded with one channel for each class/group) to 
# ITK-readable (Single channel containing multiple labels). This is mainly for visualising using ITK-SNAP app
# Works in loop for all files in a directory
import os
import nibabel as nb
import SimpleITK as sitk
%matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
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
    
    dirName = '/Users/PathTo/outs_fromMonai'
    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)
    numfiles=0
    groups=6
    # Print the files
    for elem in listOfFiles:
        if elem.endswith("T2W_seg.nii.gz"):
            print('Reading', elem)
            filename = elem[76:83]  # Edit Here based on  dirName
            im=sitk.ReadImage(elem)
            im_array=sitk.GetArrayFromImage(im)
            labelled = np.zeros([im_array.shape[1],im_array.shape[2],im_array.shape[3]])
            for i in range(groups):
                ilabel = np.squeeze(im_array[i,:,:,:])
                labelled[ilabel == 1] = i
            im_labelled = sitk.GetImageFromArray(labelled)
            sitk.WriteImage(im_labelled,f'{dirName}/PathTo/outs_ForITK/seg{filename}_T2W.nii.gz')
            numfiles+=1
            print('Saving.....')
    print(numfiles, 'files converted to ITK-readable')    
        
if __name__ == '__main__':
    main()
