""" This code can be used to convert single/multiple NIfTI image files (.nii or .ni.gz) into .png/JPEG/JPG/TIFF/TIF images. All the raw image data (.nii or .ni.gz) should be in the same folder. This code will create multiple folders with .png/JPEG/JPG/TIFF/TIF images based on the filename. Change rotation angle if required. Default is set to 90.
base source code https://github.com/alexlaurence/NIfTI-Image-Converter

Command to use this code: 

python3 nii_to_pngs_converter.py --input_path /data/path/to/you/raw_nii/files --save_image_path /path/where/you/want/to/save/the/images


"""


###########################################
# nii_to_pngs_converter.py for Python 3   #
#         NIfTI Image Converter           #
#                                         #                       
#     Written by Monjoy Saha              #
#        monjoybme@gmail.com              #
#          03 December 2021               #
#                                         #
###########################################
#import scipy.misc
import numpy, shutil, os, nibabel
import sys, getopt
import argparse
import imageio
import pdb
#############################################################
base_path=os.path.abspath(os.path.dirname(__file__))
parser = argparse.ArgumentParser(description='Arguments for input and output files')
parser.add_argument('--input_path', type=str, default = base_path, help='Path of the input files (.nii or .ni.gz')
parser.add_argument('--save_image_path', type=str, default = base_path, help='Pathto save images (.PNG or JPG or JPEG or TIFF. Change appropriate place of this code')
parser.add_argument('--rotation_angle', type=int, default = 90, help='Rotation degree, i.e., 90°, 180°, 270°, default value is 90°')
args = parser.parse_args()
input_path = args.input_path
rotation_angle = args.rotation_angle
save_image_path = args.save_image_path
##############################################################
#get list of nii or nii.gz source files
source_files = os.listdir(input_path)
slice_counter = 0
#identify sample ids and get source ids 
source_ids = [files[0:10] for files in source_files if files.endswith('.nii')] # change "files[0:10]" based on the character present in you file. In my case total character of all raw file name was within 10 character. Hence [0:10]. Change the maximum limit accordingly. #change here if the file have '.nii/.ni.gz' format

sample_ids = list(set(source_ids))

for file in sample_ids:
    fname = os.path.basename(file)
    #pdb.set_trace()
    image_array = nibabel.load(input_path + fname+'.nii').get_data() #change here if the file have '.nii/.ni.gz' format
    print(len(image_array.shape))
    # set destination folder
    if not os.path.exists(save_image_path+'/'+fname):
        os.makedirs(save_image_path+'/'+fname)
        print("Created ouput directory: " + save_image_path+'/'+fname)
    
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
                    image_name = fname[:-4] + "_z" + "{:0>3}".format(str(current_slice+1))+ ".png" #change 'PNG' to any other format such as JPG or JPEG or TIFF, etc.
                    imageio.imwrite(image_name, data)
                    print('Saved.')
                    #move images to folder
                    print('Moving image...')
                    src = image_name
                    shutil.move(src, save_image_path+'/'+fname)
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
                        image_name = fname[:-4] + "_z" + "{:0>3}".format(str(current_slice+1))+ ".png" #change 'PNG' to any other format such as JPG or JPEG or TIFF, etc.
                        imageio.imwrite(image_name, data)
                        print('Saved.')
                        #move images to folder
                        print('Moving image...')
                        src = image_name
                        shutil.move(src, save_image_path+'/'+fname)
                        slice_counter += 1
                        print('Moved.')
                        print('Finished converting images')
