# NIfTI-Image-Converter
A lightweight neuroimaging .nii to .png converter that actually works. 


1. Input 4D fMRI NIfTI file (i.e. brain.nii)
2. Automatically creates .png files for every single slice in every volume.
3. Automatically renames your images with their slice and volume name (i.e. brain_t001_z001.png, etc)
4. Automatically moves all your images into a chosen folder within your working directory.

Unlike other tools out there, this just works.

## Requirements 

* scipy
* shutil
* os
* nibabel
* numpy
