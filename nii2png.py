#!/usr/bin/python3
'''
Created by Alexander Laurence
7 May 2019
MIT License
'''

import scipy
import shutil
import os
import nibabel
import numpy

fn = input('Please enter the path of your NIfTI file: ')
wd = input('Please enter the path of your working directory: ')

# set fn as your 4d nifti file
image_array = nibabel.load(fn).get_data()

# set 4d array dimension values
nx, ny, nz, nw = image_array.shape

# set destination folder
dst = wd + "/png_" + fn[:-4]
if not os.path.exists(dst):
        os.makedirs(dst)
        print("Created ouput directory: " + dst)

print("Converting NIfTI to png...")

volumes = image_array.shape[3]
slices = image_array.shape[2]

volume_counter = 0
image_counter = 0

# iterate through volumes
for j in range(0, volumes):
  slice_counter = 0
  # iterate through slices
  for i in range(0, slices):
    # set nifti as a numpy array
    data = numpy.rot90(image_array[:, :, i, j])
    #alternate slices and save as png
    if (slice_counter % 1) == 0:
      image_name = fn[:-4] + "_t" "{:0>3}".format(str(j)) + "_z" + "{:0>3}".format(str(i))+ ".png"
      scipy.misc.imsave(image_name, data)
      
      #move images to folder
      src = "/content/" + image_name
      shutil.move(src, dst)
      slice_counter += 1
      image_counter += 1
  volume_counter += 1

print("Finished converting images") 
