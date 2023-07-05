# Version: 1.0.5
# Contributors: Arlind-dev
# Python 3.11.0

import os
from natsort import natsort_keygen
from tabulate import tabulate

# Ask the user for a directory path to work in
directory_path = input("Enter a directory path (default is current directory): ")

# Check if the user entered a value or not
if not directory_path:
    directory_path = "."  # Set default value to current directory

# Resolve the directory path to an absolute path using os.path.abspath()
directory_path = os.path.abspath(directory_path)

# Check if the directory exists
if not os.path.exists(directory_path):
    print(f"The directory {directory_path} does not exist.")
    exit()

# Create a list of all subdirectories containing "Season" in their name
season_directories = [
    d
    for d in os.listdir(directory_path)
    if os.path.isdir(os.path.join(directory_path, d)) and "Season" in d
]

# Check if there are any season directories
if not season_directories:
    print("No 'Season' directory found.")
    print("For more information check out the README")
    print("https://github.com/Arlind-dev/jellyfin-rename-videos/tree/main#requirements")
    exit()

# Ask the user for a file extension to filter by
file_ext = input("Enter a file extension (default is mkv): ")

# Set default value to mkv if the user does not enter a value
if not file_ext:
    file_ext = "mkv"

# Store the renaming information in a list of lists
renaming_info = []

# Iterate through each season directory
for season_directory in season_directories:
    season_number_str = season_directory.split()[-1]
    try:
        season_number = int(season_number_str)
    except ValueError:
        print(f"Invalid season number: {season_number_str}")
        print("'Season' directory can only contain 2 Digits (00-99)")
        continue

    season_info = []

    # List the files in the season directory with the specified extension, sorted naturally
    season_directory_path = os.path.join(directory_path, season_directory)
    natural_sort_key = natsort_keygen()
    files = sorted(
        [
            f
            for f in os.listdir(season_directory_path)
            if f.lower().endswith("." + file_ext.lower())
        ],
        key=natural_sort_key,
    )

    # Determine the number of digits needed based on the number of files
    num_digits = max(2, len(str(len(files))))

    # Construct the new file extension format string
    new_file_ext = f"S{season_number:02d}E{{:0{num_digits}d}}.{file_ext}"

    # Show the user the new filenames
    for i, filename in enumerate(files, start=1):
        old_path = os.path.join(season_directory_path, filename)
        new_filename = new_file_ext.format(i)
        new_path = os.path.join(season_directory_path, new_filename)
        rel_old_path = os.path.relpath(old_path, start=directory_path)
        rel_new_path = os.path.relpath(new_path, start=directory_path)
        season_info.append(
            [f".{os.path.sep}{rel_old_path}", f".{os.path.sep}{rel_new_path}"]
        )

    renaming_info.append(season_info)

    renamed = any(
        filename != new_file_ext.format(i) for i, filename in enumerate(files, start=1)
    )
    if not renamed:
        print(f"Episodes in {season_directory} don't need to be renamed.")
        continue

    # Print the renaming information as a table
    print(f"\nRenaming Information for {season_directory}:")
    print(
        tabulate(season_info, headers=["Old Path", "New Path"], tablefmt="fancy_grid")
    )

    # Ask the user if they want to proceed with renaming the files
    confirmation_rename = (
        input(
            f"Do you want to proceed with renaming the files in {season_directory}? (y/n): "
        )
        .strip()
        .lower()
        or "y"
    )
    if confirmation_rename != "y":
        print(f"File renaming cancelled for {season_directory}.")
        continue

    # Rename the files according to the specified naming convention
    for j, (old_path, new_path) in enumerate(season_info, start=1):
        os.rename(
            os.path.join(directory_path, old_path),
            os.path.join(directory_path, new_path),
        )

print("\nDone.")
