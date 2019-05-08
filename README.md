# NIfTI-Image-Converter
Rejoice OpenCV users, a lightweight neuroimaging .nii to .png converter that actually works. 


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

## Usage 

Let's run the file and start converting images! Please ensure that your output folder ends with a slash to avoid errors.

```
$ python3 nii2png.py -i <inputfile> -o <outputfolder>
```

or

```
$ python3 nii2png.py --input <inputfile> --ouput <outputfolder>
```

Tip: You can drag and drop the file/folder into the terminal window instead of typing the path

### Example

with change directory command

```
$ cd ~/images/
$ python3 nii2png.py -i brain.nii -o png/
```

with full paths

```
$ python3 /users/ernie/images/nii2png.py -i /users/ernie/images/brain.nii -o /users/ernie/images/png/
```

with long options


```
$ python3 /users/ernie/images/nii2png.py --input /users/ernie/images/brain.nii --output /users/ernie/images/png/
```
