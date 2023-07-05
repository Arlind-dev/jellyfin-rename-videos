# Jellyfin Rename Videos

This Python script renames video files in subdirectories named `Season YY` to the format `SYYEXX.ext`, where "YY" is the season number and "XX" is the episode number, sorted naturally.

## Requirements

- Folders that have videos in them which are already sorted the correct way: ex.
```
.
├── Season 01/
│   ├── video1.mkv
│   ├── video2.mkv
│   └── video3.mkv
└── Season 02/
    ├── video4.mkv
    ├── video5.mkv
    └── video6.mkv
```

- Python 3 (Tested on 3.8.12, 3.11.0)
- natsort package
- tabulate package

```bash
pip install tabulate
```

## Arguments

| Shorted argument | Full argument | Instructions                            |
| ---------------- | ------------- | --------------------------------------- |
| -h               | --help        | show this help message and exit         |
| -d               | --directory   | Inputs the directory to the script      |
| -e               | --extension   | Inputs the file extension to the script |

### Examples

#### Both arguments

```bash
python jellyfin_rename.py -e mp4 -d /path/to/directory
```

#### One argument

```bash
python jellyfin_rename.py -d /path/to/directory # you will need to input the file extension in the script
```

```bash
python jellyfin_rename.py -e mkv # you will need to input the directory in the script
```

## Usage

1. Clone the repository, download the script `jellyfin_rename.py` or download the newest release.
2. Open a command prompt or terminal in the directory containing the script.
3. Run the script by typing `python jellyfin_rename.py` or `python3 jellyfin_rename.py` depending on how your python is set up.
4. Enter the folder path to work in when prompted, or leave it blank for the current directory.
5. Enter the file extension to filter by when prompted, or leave it blank for `.mkv`.
6. The script will display the old and new filenames for each video file to be renamed, sorted by season and episode number. Confirm whether you want to proceed with renaming the files for each season.
7. The script will rename the files according to the specified naming convention.

You can also skip the folder path and file extension input by putting in the necessary arguments!

```bash
python jellyfin_rename.py -e mkv -d /path/to/directory
```

## Example

Suppose you have the following folder structure:

```
.
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
Enter a directory path (default is current directory):
Enter a file extension (default is mkv):

Renaming Information for Season 01:
╒════════════════════════╤════════════════════════╕
│ Old Path               │ New Path               │
╞════════════════════════╪════════════════════════╡
│ .\Season 01\video1.mkv │ .\Season 01\S01E01.mkv │
├────────────────────────┼────────────────────────┤
│ .\Season 01\video2.mkv │ .\Season 01\S01E02.mkv │
├────────────────────────┼────────────────────────┤
│ .\Season 01\video3.mkv │ .\Season 01\S01E03.mkv │
╘════════════════════════╧════════════════════════╛
Do you want to proceed with renaming the files in Season 01? (y/n):

Renaming Information for Season 02:
╒════════════════════════╤════════════════════════╕
│ Old Path               │ New Path               │
╞════════════════════════╪════════════════════════╡
│ .\Season 02\video4.mkv │ .\Season 02\S02E01.mkv │
├────────────────────────┼────────────────────────┤
│ .\Season 02\video5.mkv │ .\Season 02\S02E02.mkv │
├────────────────────────┼────────────────────────┤
│ .\Season 02\video6.mkv │ .\Season 02\S02E03.mkv │
╘════════════════════════╧════════════════════════╛
Do you want to proceed with renaming the files in Season 02? (y/n):

Done.
```
After confirming that you want to proceed with renaming the files for each season, the script will rename the files as follows:

```
.
├── Season 01/
│   ├── S01E01.mkv
│   ├── S01E02.mkv
│   └── S01E03.mkv
└── Season 02/
    ├── S02E01.mkv
    ├── S02E02.mkv
    └── S02E03.mkv
```

## Contributions

Contributions to this project are welcome and greatly appreciated. If you find any bugs or have suggestions for new features, please create an issue or a pull request on the project's GitHub repository.

Feel free to fork this repository and modify it to fit your needs. If you do so, please credit the original repository and consider opening a pull request to contribute your changes back upstream.


## License

This project is licensed under the MIT License.
