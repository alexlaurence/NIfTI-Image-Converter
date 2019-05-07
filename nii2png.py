#!/usr/bin/python3
'''
NIfTI Image Converter (v0.1.6)
Created by Alexander Laurence
7 May 2019
MIT License
'''

import scipy
import shutil
import os
import nibabel
import numpy

def convert():
        fn = input('Firstly, please enter the path of your NIfTI file: ')
        wd = input('Next, please enter the path of your working directory: ')
        od = input('Finally, please enter the name for your output folder: ')

        # set fn as your 4d nifti file
        image_array = nibabel.load(fn).get_data()

        # if 4D image inputted
        if len(image_array) == 4:
                # set 4d array dimension values
                nx, ny, nz, nw = image_array.shape

                # set destination folder
                dst = wd + "/" + od + "_" + fn[:-4]
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
                      src = wd + image_name
                      shutil.move(src, dst)
                      slice_counter += 1
                      image_counter += 1
                  volume_counter += 1

                print("Finished converting images") 

        # else if 3D image inputted
        elif len(image_array) == 3:
                # set 4d array dimension values
                nx, ny, nz = image_array.shape

                # set destination folder
                dst = wd + "/" + od + "_" + fn[:-4]
                if not os.path.exists(dst):
                        os.makedirs(dst)
                        print("Created ouput directory: " + dst)

                print("Converting NIfTI to png...")

                slices = image_array.shape[2]

                image_counter = 0
                slice_counter = 0
                # iterate through slices
                for i in range(0, slices):
                        # set nifti as a numpy array
                        data = numpy.rot90(image_array[:, :, i])
                        #alternate slices and save as png
                        if (slice_counter % 1) == 0:
                                image_name = fn[:-4] + "_z" + "{:0>3}".format(str(i))+ ".png"
                                scipy.misc.imsave(image_name, data)

                                #move images to folder
                                src = wd + image_name
                                shutil.move(src, dst)
                                slice_counter += 1
                                image_counter += 1

                print("Finished converting images") 
        else:
                print("Not a 3D or 4D Image. Please try again.")
                convert()

# call the function to start the program
convert()
