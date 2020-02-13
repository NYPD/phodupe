# phodupe

## What is it

A simple little python script that finds duplicate file names (without the extension) across multiple directories (and recursively if set) and gives the user the option to delete them.

## Why

I used this as an opportunity to begin learning python. It was created for a very very specific scenario and might not be too useful to anyone else.

## How do to install / run

(There are probably better ways to run this, but i'm a python noob)

- Navigate to the folder you downloaded the git project to
  - `cd \development\git\Phodupe\`
- Install the python script
  - `python .\setup.py install`
- Run the script by passing a source directory and any number of "delete" directories
  - Deletes dupes from OG Phone Walls and 2Delete:
    - `python phodupe "C:\Users\NYPD\Desktop\OG Phone Walls" "C:\Users\NYPD\Desktop\2Delete"`
  - Deletes dupes from OG Phone Walls, 2Delete , and AlsoDelete:
    - `python phodupe "C:\Users\NYPD\Desktop\OG Phone Walls" "C:\Users\NYPD\Desktop\2Delete" "C:\Users\NYPD\Desktop\AlsoDelete"`