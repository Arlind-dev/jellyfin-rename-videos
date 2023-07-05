# Version: 2.0.0
# Contributors: Arlind-dev

import os
from natsort import natsort_keygen
from tabulate import tabulate


def get_directory_path():
    # Prompt the user to enter a directory path
    while True:
        directory_path = input(
            "Enter a directory path (default is current directory): "
        )
        if not directory_path:
            directory_path = "."  # Set the default value to current directory
        if os.path.exists(directory_path):
            return directory_path
        else:
            print("Invalid directory path. Please try again.")


def get_season_directories(directory_path):
    # Get the 'Season' directories in the given directory
    season_directories = [
        d
        for d in os.listdir(directory_path)
        if os.path.isdir(os.path.join(directory_path, d))
        and d.lower().startswith("season")
    ]
    return season_directories


def print_season_directory_not_found_message():
    # Print a message if no 'Season' directory is found
    print(
        "No 'Season' directory found.\nFor more information, please check out the README:\nhttps://github.com/Arlind-dev/jellyfin-rename-videos/tree/main#requirements"
    )


def get_file_extension():
    # Prompt the user to enter a file extension
    while True:
        file_ext = input("Enter a file extension (default is mkv): ") or "mkv"

        if file_ext.isalnum():
            return file_ext
        else:
            print("Invalid file extension. Only letters and numbers are allowed.")


def get_season_number(season_directory):
    # Extract the season number from the 'Season' directory name
    try:
        season_number = int(season_directory.split()[-1])
        return season_number
    except ValueError:
        print(f"Invalid season: '{season_directory}'")
        print("'Season' directory must contain a valid integer season number.")
        return None


def list_files_in_season_directory(season_directory_path, file_ext):
    # List the files with the given file extension in the 'Season' directory
    files = sorted(
        [
            f
            for f in os.listdir(season_directory_path)
            if f.lower().endswith("." + file_ext.lower())
        ]
    )
    return files


def rename_file_extension(directory_path, season_directory, file_ext):
    # Rename the file extension of the files in the 'Season' directory to lowercase
    season_directory_path = os.path.join(directory_path, season_directory)
    files = list_files_in_season_directory(season_directory_path, file_ext)
    renamed_files = []

    for filename in files:
        new_filename = filename.lower()
        if new_filename != filename:
            old_path = os.path.join(season_directory_path, filename)
            new_path = os.path.join(season_directory_path, new_filename)
            os.rename(old_path, new_path)
            renamed_files.append(filename)

    if renamed_files:
        rel_directory_path = os.path.relpath(
            season_directory_path, start=directory_path
        )
        print(
            f"Made file extensions lowercase in the directory: .{os.sep}{rel_directory_path}"
        )


def construct_new_file_extension(season_number, num_digits, file_ext):
    # Construct the new file extension format based on the season number and the number of files
    season_number_str = str(season_number).zfill(2)
    new_file_ext = f"S{season_number_str}E{{:0{num_digits}d}}.{file_ext}"
    return new_file_ext


def get_renaming_info(directory_path, season_directory, file_ext):
    # Get the renaming information for the files in the 'Season' directory
    season_directory_path = os.path.join(directory_path, season_directory)
    files = list_files_in_season_directory(season_directory_path, file_ext)

    season_number = get_season_number(season_directory)
    if season_number is None:
        return None, None, None

    new_file_ext = construct_new_file_extension(season_number, len(files), file_ext)

    season_info = [
        [
            f".{os.path.sep}{os.path.relpath(os.path.join(season_directory_path, filename), start=directory_path)}",
            f".{os.path.sep}{os.path.relpath(os.path.join(season_directory_path, new_file_ext.format(i)), start=directory_path)}",
        ]
        for i, filename in enumerate(files, start=1)
    ]

    return season_info, new_file_ext, files


def rename_files(directory_path, season_info):
    # Rename the files based on the renaming information
    for old_path, new_path in season_info:
        os.rename(
            os.path.join(directory_path, old_path),
            os.path.join(directory_path, new_path),
        )


def main():
    # Main function to execute the file renaming process
    directory_path = get_directory_path()
    season_directories = get_season_directories(directory_path)

    if not season_directories:
        print_season_directory_not_found_message()
        return

    file_ext = get_file_extension()

    for season_directory in season_directories:
        rename_file_extension(directory_path, season_directory, file_ext)
        season_info, new_file_ext, files = get_renaming_info(
            directory_path, season_directory, file_ext
        )

        if season_info is None:
            continue

        renamed = any(
            filename != new_file_ext.format(i)
            for i, filename in enumerate(files, start=1)
        )

        if not renamed:
            print(f"Episodes in {season_directory} don't need to be renamed.")
            continue

        print(f"\nRenaming Information for {season_directory}:")
        print(
            tabulate(
                season_info, headers=["Old Path", "New Path"], tablefmt="fancy_grid"
            )
        )

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

        rename_files(directory_path, season_info)

    print("\nDone.")


if __name__ == "__main__":
    main()
