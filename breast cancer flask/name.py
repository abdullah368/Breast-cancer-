import os

# Directory containing the files
directory = r'D:\Final year Project\good'

# Starting index for renaming
start_index = 34

# Iterate over files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.png') or filename.endswith('.tif'):
        # Generate the new filename
        new_filename = f'g ({start_index}).png'
        
        # Construct the full path of the file
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_path, new_path)
        
        # Increment the index for the next file
        start_index += 1
