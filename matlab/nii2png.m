%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%       nii2png for Matlab R2017b       %
%         NIfTI Image Converter         %
%                v0.2.9                 %
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
   
   % ask user to rotate and by how much
   ask_rotate = input(' Would you like to rotate the orientation? (y/n) ', 's');
   if lower(ask_rotate) == 'y'
       ask_rotate_num = str2double(input('OK. By 90° 180° or 270°? ', 's'));
       if ask_rotate_num == 90 || ask_rotate_num == 180 || ask_rotate_num == 270
           disp('Got it. Your images will be rotated.');
       else
           disp('Sorry, I did not understand that. Quitting...');
           exit;
       end
   elseif lower(ask_rotate) ~= 'n' && lower(ask_rotate) ~= 'y'
       disp('Sorry, I did not understand that. Quitting...');
       exit;
   end

   % If this is a 4D NIfTI
   if length(nifti_array) == 4
       
       % Create output folder
       mkdir png
       
       % Get Vols and Slice
       total_volumes = nifti_array(4);
       total_slices = nifti_array(3);
       
       current_volume = 1;
       disp('Converting NIfTI to png, please wait...')
       % Iterate Through Vol
       while current_volume <= total_volumes
           slice_counter = 0;
            % Iterate Through Slices
            current_slice = 1;
            while current_slice <= total_slices
                % Alternate Slices
                if mod(slice_counter, 1) == 0
                    
                    % Rotate images if selected
                    if lower(ask_rotate) == 'y'
                        if ask_rotate_num == 90
                            data = rot90(mat2gray(double(:,:,current_slice,current_volume)));
                        elseif ask_rotate_num == 180
                            data = rot90(rot90(mat2gray(double(:,:,current_slice,current_volume))));
                        elseif ask_rotate_num == 270
                            data = rot90(rot90(rot90(mat2gray(double(:,:,current_slice,current_volume)))));
                        end
                    elseif lower(ask_rotate) == 'n'
                    disp('OK, I will convert it as it is.');
                    data = mat2gray(double(:,:,current_slice,current_volume));
                    end
                    
                    % Set Filename as per slice and vol info
                    filename = file(1:end-4) + "_t" + sprintf('%03d', current_volume) + "_z" + sprintf('%03d', current_slice) + ".png";
                    
                    % Write Image
                    imwrite(data, char(filename));
                                        
                    % If we reached the end of the slices
                    if current_slice == total_slices
                        % But not the end of the volumes
                        if current_volume < total_volumes
                            % Move to the next volume                            
                            current_volume = current_volume + 1;
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
                    
                    percentage = strcat('Please wait. Converting...', ' ', num2str((current_volume/total_volumes)*100), '% Complete');
                    
                    if ((current_volume/total_volumes)*100) == 100
                        disp('100% Complete! Images successfully converted.');
                    else
                        disp(percentage);
                    end                    
                end
                current_slice = current_slice + 1;
            end
       current_volume = current_volume + 1;
       end
   % Else if this is a 3D NIfTI
   elseif length(nifti_array) == 3
       % Create output folder
       mkdir png
       
       % Get Vols and Slice
       total_slices = nifti_array(3);
       
       disp('Converting NIfTI to png, please wait...')

       slice_counter = 0;
        % Iterate Through Slices
        current_slice = 1;
        while current_slice <= total_slices
            % Alternate Slices
            if mod(slice_counter, 1) == 0     
                
                % Rotate images if selected
                if lower(ask_rotate) == 'y'
                    if ask_rotate_num == 90
                        data = rot90(mat2gray(double(:,:,current_slice)));
                    elseif ask_rotate_num == 180
                        data = rot90(rot90(mat2gray(double(:,:,current_slice))));
                    elseif ask_rotate_num == 270
                        data = rot90(rot90(rot90(mat2gray(double(:,:,current_slice)))));
                    end
                elseif lower(ask_rotate) == 'n'
                disp('OK, I will convert it as it is.');
                data = mat2gray(double(:,:,current_slice));
                end
                
                % Set Filename as per slice and vol info
                filename = file(1:end-4) + "_z" + sprintf('%03d', current_slice) + ".png";

                % Write Image
                imwrite(data, char(filename));

                % Move Images To Folder
                movefile(char(filename),'png');

                % Increment Counters
                slice_counter = slice_counter + 1;

                percentage = strcat('Please wait. Converting...', ' ', num2str((current_slice/total_slices)*100), '% Complete');

                if ((current_slice/total_slices)*100) == 100
                    disp('100% Complete! Images successfully converted');
                else
                    disp(percentage);
                end                    
            end
            current_slice  = current_slice  + 1;
        end
   elseif length(nifti_array) ~= 3 || 4
       disp('NIfTI must be 3D or 4D. Please try again.');
   end
end
