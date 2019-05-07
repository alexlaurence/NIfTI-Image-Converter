# NIfTI-Image-Converter
A lightweight neuroimaging .nii to .png converter that actually works. 


1. Input 4D fMRI NIfTI file (i.e. brain.nii)
2. Automatically creates .png files for every single slice in every volume.
3. Automatically renames your images with their slice and volume name (i.e. brain_t001_z001.png, etc)
4. Automatically moves all your images into a chosen folder within your working directory.

Unlike other tools out there, this just works.

## Environment
* Python 3.7

## Modules 
* scipy
* shutil
* os
* nibabel
* numpy

## Basic Setup

For those without Python, Pip or the modules, simply open Terminal and type in the following commands and hit enter.

Install Python

`brew install python3`

Install pip

`sudo easy_install pip`

Install plugins

`pip install scipy`
`pip install shutil`
`pip install os`
`pip install nibabel`
`pip install numpy`

## Running The File

Let's run the file and start converting images!

`cd /folder/where/the/.py/file/is

python3 nii2png.py
`
When it asks you for file/folder paths, you can drag and drop the file/folder into the terminal window and hit enter.
