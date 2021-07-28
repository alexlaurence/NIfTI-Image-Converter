""" This code can be used to convert single/multiple NIfTI image files (.nii or .ni.gz) into .png images. Set the input file path and rotation angle to get the PNGs.
    base source code https://github.com/alexlaurence/NIfTI-Image-Converter"""

###########################################
# nii_to_pngs_converter.py for Python 3   #
#         NIfTI Image Converter           #
#                                         #                       
#     Written by Monjoy Saha              #
#        monjoybme@gmail.com              #
#          02 July 2020                   #
#                                         #
###########################################
#import scipy.misc
import numpy, shutil, os, nibabel
import sys, getopt
import argparse
import imageio

#############################################################
base_path=os.path.abspath(os.path.dirname(__file__))
parser = argparse.ArgumentParser(description='Arguments for input and output files')
parser.add_argument('--input_path', type=str, default = base_path, help='Path of the input files')
parser.add_argument('--rotation_angle', type=int, default = 90, help='Rotation degree, i.e., 90°, 180°, 270°, default value is 90°')
args = parser.parse_args()
input_path = args.input_path
rotation_angle = args.rotation_angle
##############################################################
#get list of nii or nii.gz source files
source_files = os.listdir(input_path)
slice_counter = 0
#identify sample ids and get source ids 
source_ids = [files[0:8] for files in source_files if files.endswith('.nii')]

sample_ids = list(set(source_ids))

for file in sample_ids:
    fname = os.path.basename(file)
    image_array = nibabel.load(fname+'.nii').get_data()
    print(len(image_array.shape))
    # set destination folder
    if not os.path.exists(base_path+'/'+fname):
        os.makedirs(base_path+'/'+fname)
        print("Created ouput directory: " + base_path+'/'+fname)
    
    # For 3D image inputted    
    if len(image_array.shape) == 3:
        nx, ny, nz = image_array.shape
        total_slices = image_array.shape[2]
        # iterate through slices
        for current_slice in range(0, total_slices):
            # alternate slices
            if (slice_counter % 1) == 0:
                # rotate or no rotate
                if rotation_angle == 90:
                    data = numpy.rot90(image_array[:, :, current_slice])
                elif rotation_angle == 180:
                    data = numpy.rot90(numpy.rot90(image_array[:, :, current_slice]))
                elif rotation_angle == 270:
                    data = numpy.rot90(numpy.rot90(numpy.rot90(image_array[:, :, current_slice])))
                 #alternate slices and save as png
                if (slice_counter % 1) == 0:
                    print('Saving image...')
                    image_name = fname[:-4] + "_z" + "{:0>3}".format(str(current_slice+1))+ ".png"
                    imageio.imwrite(image_name, data)
                    print('Saved.')
                    #move images to folder
                    print('Moving image...')
                    src = image_name
                    shutil.move(src, base_path+'/'+fname)
                    slice_counter += 1
                    print('Moved.')
                    print('Finished converting images')
    elif len(image_array.shape) == 4:
        nx, ny, nz, nw = image_array.shape
        total_volumes = image_array.shape[3]
        total_slices = image_array.shape[2]
        for current_volume in range(0, total_volumes):
            # iterate through slices
            for current_slice in range(0, total_slices):
                if (slice_counter % 1) == 0:
                    if rotation_angle == 90:
                        data = numpy.rot90(image_array[:, :, current_slice, current_volume])
                    elif rotation_angle == 180:
                        data = numpy.rot90(numpy.rot90(image_array[:, :, current_slice, current_volume]))
                    elif rotation_angle == 270:
                        data = numpy.rot90(numpy.rot90(numpy.rot90(image_array[:, :, current_slice, current_volume])))

                    #alternate slices and save as png
                    if (slice_counter % 1) == 0:
                        print('Saving image...')
                        image_name = fname[:-4] + "_z" + "{:0>3}".format(str(current_slice+1))+ ".png"
                        imageio.imwrite(image_name, data)
                        print('Saved.')
                        #move images to folder
                        print('Moving image...')
                        src = image_name
                        shutil.move(src, base_path+'/'+fname)
                        slice_counter += 1
                        print('Moved.')
                        print('Finished converting images')

