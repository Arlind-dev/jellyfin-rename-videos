# Jellyfin Rename Videos

This Python script renames video files in subdirectories named `Season YY` to the format `SEYYEPXX.ext`, where "YY" is the season number and "XX" is the episode number, sorted naturally.

## Requirements

- Python 3 (only tested on python 3.11.0)
- natsort package

```bash
pip install natsort
```

## Usage

1. Clone the repository or download the script `jellyfin_rename.py`.
2. Open a command prompt or terminal in the directory containing the script.
3. Run the script by typing `python jellyfin_rename.py` or `python3 jellyfin_rename.py` depending on how your python is set up.
4. Enter the folder path to work in when prompted, or leave it blank for the current directory.
5. Enter the file extension to filter by when prompted, or leave it blank for `.mkv`.
6. The script will display the old and new filenames for each video file to be renamed, sorted by season and episode number. Confirm whether you want to proceed with renaming the files for each season.
7. The script will rename the files according to the specified naming convention.

## Example

Suppose you have the following folder structure:

```bash
jellyfin_rename_videos/
├── Season 01/
│   ├── video1.mkv
│   ├── video2.mkv
│   └── video3.mkv
└── Season 02/
    ├── video4.mkv
    ├── video5.mkv
    └── video6.mkv
```

You run the script by typing `python jellyfin_rename_videos.py`, and enter `mkv` (or leave it blank) for the file extension. The script will display the following:

```
Enter a folder path (default is current directory):

Enter a file extension (default is mkv):

./Season 01/video1.mkv --> ./Season 01/SE01EP01.mkv
./Season 01/video2.mkv --> ./Season 01/SE01EP02.mkv
./Season 01/video3.mkv --> ./Season 01/SE01EP03.mkv
Do you want to proceed with renaming the files in Season 01? (y/n):
Done renaming files in Season 01.

./Season 02/video4.mkv --> ./Season 02/SE02EP01.mkv
./Season 02/video5.mkv --> ./Season 02/SE02EP02.mkv
./Season 02/video6.mkv --> ./Season 02/SE02EP03.mkv
Do you want to proceed with renaming the files in Season 02? (y/n):
Done renaming files in Season 02.

All files renamed.
```
After confirming that you want to proceed with renaming the files for each season, the script will rename the files as follows:

```bash
jellyfin_rename_videos/
├── Season 01/
│   ├── SE01EP01.mkv
│   ├── SE01EP02.mkv
│   └── SE01EP03.mkv
└── Season 02/
    ├── SE02EP01.mkv
    ├── SE02EP02.mkv
    └── SE02EP03.mkv
```
