%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%       nii2png for Matlab R2017b       %
%         NIfTI Image Converter         %
%                v0.1.1                 %
%                                       %
%     Written by Alexander Laurence     %
% http://Celestial.Tokyo/~AlexLaurence/ %
%    alexander.adamlaurence@gmail.com   %
%              09 May 2019              %
%              MIT License              %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Set the Working Directory
clear; warning off; current = pwd;
path = uigetdir(pwd,'select your working directory');
cd(path);

% Select NIfTI
[file,path] = uigetfile('*.nii');
if isequal(file,0)
   disp('User selected Cancel');
else
   disp(['User selected ', fullfile(path,file)]);
   
   % Read NIfTI Data and Header Info
   image = niftiread(fullfile(path,file));
   image_info = niftiinfo(fullfile(path,file));
   nifti_array = size(image);
   double = im2double(image);
   
    # set rotations
   data_4d = mat2gray(double(:,:,i,j))
   data_90_4d = rot90(data_4d)
   data_180_4d = rot90(data_90_4d)
   data_270_4d = rot90(data_180_4d)

   data_3d = mat2gray(double(:,:,i))
   data_90_3d = rot90(data_3d)
   data_180_3d = rot90(data_90_3d)
   data_270_3d = rot90(data_180_3d)

   ask_rotate = input(' Would you like to rotate the orientation? (y/n) ', 's')

  if lower(ask_rotate) == 'y'
          ask_rotate_num = input('OK. By 90° 180° or 270°? ', 's')

          if ask_rotate_num == 90
                  if length(nifti_array) == 4
                          data = data_90_4d;
                  elseif length(nifti_array) == 3
                          data = data_90_3d;
          elseif ask_rotate_num == 180
                  if length(nifti_array) == 4
                          data = data_180_4d;
                  elseif length(nifti_array) == 3
                          data = data_180_3d;
            elseif ask_rotate_num == 270
                  if length(nifti_array) == 4
                          data = data_270_4d;
                  elseif length(nifti_array) == 3
                          data = data_270_3d;
          else:
                  disp('Sorry, I did not understand that. Quitting...')
                  exit
  elseif lower(ask_rotate) == 'n'
          disp('OK, I will convert it as it is.');
          if length(nifti_array) == 4
                  data = data_4d;
          elseif length(nifti_array) == 3
                  data = data_3d;
  else:
          disp('Sorry, I did not understand that. Quitting...')
          exit

   % If this is a 4D NIfTI
   if length(nifti_array) == 4
       
       % Create output folder
       mkdir png
       
       % Get Vols and Slice
       volumes = nifti_array(4);
       slices = nifti_array(3);      
       
       disp('Converting NIfTI to png, please wait...')
       % Iterate Through Vol
       j = 1 ;
       while j <= volumes
           slice_counter = 0;
            % Iterate Through Slices
            i = 1;
            while i <= slices
                % Alternate Slices
                if mod(slice_counter, 1) == 0        
                    % Set Filename as per slice and vol info
                    filename = file(1:end-4) + "_t" + sprintf('%03d', j) + "_z" + sprintf('%03d', i) + ".png";
                    
                    % Write Image
                    imwrite(data, char(filename));
                                        
                    % If we reached the end of the slices
                    if i == slices
                        % But not the end of the volumes
                        if j < volumes
                            % Move to the next volume                            
                            j = j + 1;
                            % Write the image
                            imwrite(data, char(filename));
                        % Else if we reached the end of slice and volume
                        else         
                            % Write Image
                            imwrite(data, char(filename));
                            disp('Finished!')
                            return
                        end
                    end
                 
                    % Move Images To Folder
                    movefile(char(filename),'png');
                    
                    % Increment Counters
                    slice_counter = slice_counter + 1;
                    
                    percentage = strcat('Please wait. Converting...', ' ', num2str((j/volumes)*100), '% Complete');
                    
                    if ((j/volumes)*100) == 100
                        disp('100% Complete!');
                    else
                        disp(percentage);
                    end                    
                end
                i = i + 1;
            end
       j = j + 1;
       end
   % Else if this is a 3D NIfTI
   elseif length(nifti_array) == 3
       % Create output folder
       mkdir png
       
       % Get Vols and Slice
       slices = nifti_array(3);      
       
       disp('Converting NIfTI to png, please wait...')

       slice_counter = 0;
        % Iterate Through Slices
        i = 1;
        while i <= slices
            % Alternate Slices
            if mod(slice_counter, 1) == 0        
                % Set Filename as per slice and vol info
                filename = file(1:end-4) + "_z" + sprintf('%03d', i) + ".png";

                % Write Image
                imwrite(data, char(filename));

                % Move Images To Folder
                movefile(char(filename),'png');

                % Increment Counters
                slice_counter = slice_counter + 1;

                percentage = strcat('Please wait. Converting...', ' ', num2str((j/volumes)*100), '% Complete');

                if ((j/volumes)*100) == 100
                    disp('100% Complete!');
                else
                    disp(percentage);
                end                    
            end
            i = i + 1;
        end
   elseif length(nifti_array) ~= 3 || 4
       disp('NIfTI must be 3D or 4D. Please try again.');
   end
end
