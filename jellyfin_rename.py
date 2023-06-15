# Version: 1.0.0
# Author: Arlind-dev
# Python 3.11.0

import os
from natsort import natsort_keygen

# Ask the user for a folder path to work in
folder_path = input("Enter a folder path (default is current directory): ")

# Check if the user entered a value or not
if not folder_path:
    folder_path = "."  # Set default value to current directory

# Resolve the folder path to an absolute path using os.path.abspath()
folder_path = os.path.abspath(folder_path)

# Check if the folder exists
if not os.path.exists(folder_path):
    print(f"The folder {folder_path} does not exist.")
    exit()

# Ask the user for a file extension to filter by
file_ext = input("Enter a file extension (default is mkv): ")

# Set default value to mkv if the user does not enter a value
if not file_ext:
    file_ext = "mkv"

# Create a list of all subdirectories containing "Season" in their name
season_dirs = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d)) and "Season" in d]

# Iterate through each season directory
for season_dir in season_dirs:
    season_number_str = season_dir.split()[-1]
    try:
        season_number = int(season_number_str)
    except ValueError:
        print(f"Invalid season number: {season_number_str}")
        continue

    # List the files in the season directory with the specified extension, sorted naturally
    season_dir_path = os.path.join(folder_path, season_dir)
    nkey = natsort_keygen()
    files = sorted([f for f in os.listdir(season_dir_path) if f.lower().endswith("." + file_ext.lower())], key=nkey)

    # Check if the number of files is a three-digit number
    if len(files) > 99:
        new_file_ext = f"SE{season_number:02d}EP{{:03d}}.{file_ext}"
    else:
        new_file_ext = f"SE{season_number:02d}EP{{:02d}}.{file_ext}"

    # Show the user the new filenames
    for i, filename in enumerate(files, start=1):
        old_path = os.path.join(season_dir_path, filename)
        new_filename = new_file_ext.format(i)
        new_path = os.path.join(season_dir_path, new_filename)
        rel_old_path = os.path.relpath(old_path, start=folder_path)
        rel_new_path = os.path.relpath(new_path, start=folder_path)
        print(f".{os.path.sep}{rel_old_path} --> .{os.path.sep}{rel_new_path}")

    # Ask the user if they want to proceed with renaming the files
    confirmationRename = input(f"Do you want to proceed with renaming the files in {season_dir}? (y/n): ").strip().lower() or "y"
    if confirmationRename != "y":
        print(f"File renaming cancelled for {season_dir}.")
        continue

    # Rename the files according to the specified naming convention
    for i, filename in enumerate(files, start=1):
        old_path = os.path.join(season_dir_path, filename)
        new_filename = new_file_ext.format(i)
        new_path = os.path.join(season_dir_path, new_filename)
        os.rename(old_path, new_path)

print("done")
