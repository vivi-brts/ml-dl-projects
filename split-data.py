import os
import shutil
import random


def copy_images(src_folder, dest_folder, num_files=1000):
    # Ensure destination folder exists
    os.makedirs(dest_folder, exist_ok=True)

    # List all files in the source folder (only files, no directories)
    files = [f for f in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, f))]

    # Debug: Print the number of files found
    print(f"Found {len(files)} files in source folder.")

    if len(files) == 0:
        print("No files found in source folder.")
        return

    # Select the first `num_files` files
    files_to_copy = files[:num_files]

    # Debug: Print the names of the files to copy
    print(f"Copying the following files: {files_to_copy}")

    for file in files_to_copy:
        src_file = os.path.join(src_folder, file)
        dest_file = os.path.join(dest_folder, file)

        try:
            # Copy the file from the source folder to the destination folder
            shutil.copy(src_file, dest_file)
            print(f"Copied: {file}")  # Print each copied file
        except Exception as e:
            print(f"Failed to copy {file}: {e}")

    print(f"{num_files} files have been copied to {dest_folder}")

src_folder = 'C:/Users/barti/Downloads/Dataset/Train/Fake'  # Replace with the path using "/" format to your source folder
dest_folder = 'C:/Users/barti/git-repo/ml-dl-projects/dataset/fake'       # Replace with the path where you want to create the 'dataset' folder 

# Run copy command
if __name__ == "__main__":
    copy_images(src_folder, dest_folder, num_files=1000)