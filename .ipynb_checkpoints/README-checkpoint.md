# NIfTI Image Converter (nii2png) for Python and Matlab
Rejoice OpenCV users, a lightweight neuroimaging .nii to .png converter that actually works. 

Now supports both Python3 and Matlab 2017b!

## Environment
* Python 3.7 (or Matlab 2017b)

# Matlab Usage
1. Add your script to your path. And run it simply by typing this and hitting enter:
```
nii2png
```
2. Select your working directory.
3. Select your NIfTI image.
4. Rotate your image if you wish:
```
>> Would you like to rotate the orientation? (y/n)
>> y
>> OK. By 90° 180° or 270°? 
>> 90
```
5. Let it run.
6. Your png files are now in the png folder of your working directory.

## Download nii2png for Matlab 2017b
Download Latest Build: [Download](https://raw.githubusercontent.com/alexlaurence/NIfTI-Image-Converter/master/matlab/nii2png.m)

Download Stable Release: [Download](https://github.com/alexlaurence/NIfTI-Image-Converter/releases)

# Python Setup

For those without Python, Pip or the modules, simply open Terminal and type in the following commands and hit enter.

1. Install Homebrew
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
2. Install Python 3
```
brew install python3
```
3. Install pip
```
sudo easy_install pip
```
4. Install plugins

```
pip install scipy

pip install shutil

pip install nibabel

pip install numpy

pip install imageio
```

## Download nii2png for Python
You can download the latest version of nii2png through pip.
```
pip install nii2png
```
Or alternatively, download the binary files here.

Download Latest Build: [Download](https://raw.githubusercontent.com/alexlaurence/NIfTI-Image-Converter/master/python/nii2png.py)

Download Stable Release: [Download](https://github.com/alexlaurence/NIfTI-Image-Converter/releases)

## Permissions

If you didn't install nii2png through pip, you may need to grant nii2png.py permission to execute. On unix systems, Python scripts can be made executable using the following process:

```
$ chmod +x nii2png.py
```

Optional: You can also move `nii2png.py` into your bin directory, and it will be runnable from anywhere.


## Python Usage 

1. Let's run the file and start converting images! Please ensure that your output folder ends with a slash to avoid errors.

```
$ python3 nii2png.py -i <inputfile> -o <outputfolder>
```

or

```
$ python3 nii2png.py --input <inputfile> --ouput <outputfolder>
```

Tip: You can drag and drop the file/folder into the terminal window instead of typing the path

2. Rotate the images if you wish

```
$ Would you like to rotate the orientation? (y/n) y
$ OK. By 90° 180° or 270°? 90
```

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
