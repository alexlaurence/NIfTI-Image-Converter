#!/usr/bin/python3.7
'''''''''''''''''''''''''''''''''''''''''
'       nii2png for Python 3.7          '
'         NIfTI Image Converter         '
'                v0.2.7                 '
'                                       '
'     Written by Alexander Laurence     '
' http://Celestial.Tokyo/~AlexLaurence/ '
'    alexander.adamlaurence@gmail.com   '
'              09 May 2019              '
'              MIT License              '
'''''''''''''''''''''''''''''''''''''''''

import scipy, numpy, shutil, os, nibabel
import sys, getopt

def main(argv):
        
        inputfile = ''
        outputfile = ''
        try:
                opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
        except getopt.GetoptError:
                print('nii2png.py -i <inputfile> -o <outputfile>')
                sys.exit(2)
        for opt, arg in opts:
                if opt == '-h':
                        print('nii2png.py -i <inputfile> -o <outputfile>')
                        sys.exit()
                elif opt in ("-i", "--input"):
                        inputfile = arg
                elif opt in ("-o", "--output"):
                        outputfile = arg
        print('Input file is ', inputfile)
        print('Output folder is ', outputfile)

        # set fn as your 4d nifti file
        image_array = nibabel.load(inputfile).get_data()
        print(len(image_array.shape))
        
        # set rotations
        data_4d = image_array[:, :, i, j]
        data_rot1_4d = numpy.rot90(image_array[:, :, i, j])
        data_rot2_4d = numpy.rot90(data_rot1_4d)
        data_rot3_4d = numpy.rot90(data_rot2_4d)
        
        data_3d = image_array[:, :, i]
        data_rot1_3d = numpy.rot90(image_array[:, :, i])
        data_rot2_3d = numpy.rot90(data_rot1_3d)
        data_rot3_3d = numpy.rot90(data_rot2_3d)
        
        ask_rotate = input('Would you like to rotate the orientation? (y/n) ')
        
        if ask_rotate.lower() == 'y':
                ask_rotate_num = input('OK. By 90° 180° or 270°? ')
                
                if ask_rotate_num == 90:
                        if len(image_array.shape) == 4:
                                data = data_rot1_4d
                        elif len(image_array.shape) == 3:
                                data = data_rot1_3d
                elif ask_rotate_num == 180:
                        if len(image_array.shape) == 4:
                                data = data_rot2_4d
                        elif len(image_array.shape) == 3:
                                data = data_rot2_3d
                elif ask_rotate_num == 280: 
                        if len(image_array.shape) == 4:
                                data = data_rot3_4d
                        elif len(image_array.shape) == 3:
                                data = data_rot3_3d
                else:
                        print('Sorry, I did not understand that. Quitting...')
                        sys.exit()
        elif ask_rotate.lower() == 'n':
                print('OK, I will convert it as it is.')
                if len(image_array.shape) == 4:
                        data = data_4d
                elif len(image_array.shape) == 3:
                        data = data_3d
        else:
                print('Sorry, I did not understand that. Quitting...')
                sys.exit()

        # if 4D image inputted
        if len(image_array.shape) == 4:
                # set 4d array dimension values
                nx, ny, nz, nw = image_array.shape

                # set destination folder
                if not os.path.exists(outputfile):
                        os.makedirs(outputfile)
                        print("Created ouput directory: " + outputfile)

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
                    #alternate slices and save as png
                    if (slice_counter % 1) == 0:
                      image_name = inputfile[:-4] + "_t" + "{:0>3}".format(str(j)) + "_z" + "{:0>3}".format(str(i))+ ".png"
                      scipy.misc.imsave(image_name, data)

                      #move images to folder
                      src = image_name
                      shutil.move(src, outputfile)
                      slice_counter += 1
                      image_counter += 1
                  volume_counter += 1

                print("Finished converting images") 

        # else if 3D image inputted
        elif len(image_array.shape) == 3:
                # set 4d array dimension values
                nx, ny, nz = image_array.shape

                # set destination folder
                if not os.path.exists(outputfile):
                    os.makedirs(outputfile)
                    print("Created ouput directory: " + outputfile)

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
                                image_name = inputfile[:-4] + "_z" + "{:0>3}".format(str(i))+ ".png"
                                scipy.misc.imsave(image_name, data)

                                #move images to folder
                                src = image_name
                                shutil.move(src, outputfile)
                                slice_counter += 1
                                image_counter += 1

                print("Finished converting images") 
        else:
                print("Not a 3D or 4D Image. Please try again.")

# call the function to start the program
if __name__ == "__main__":
   main(sys.argv[1:])
