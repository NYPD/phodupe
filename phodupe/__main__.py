import sys
from phodupe.dupe_finder import DupeFinder


def main():

    destination1 = sys.argv[1]
    destination2 = sys.argv[2]
    
    dupe_files = DupeFinder.getDuplicateFileNames(destination1, destination2, False)

    if len(dupe_files) is 0:
        print('No dupe files found!')
        exit()

    user_input = input("{} duplicate file names found. Enter 'y' to delete or 'n' to abort:\n".format(len(dupe_files)))
    
    if user_input == 'y':
        DupeFinder.deleteFiles(dupe_files, destination1, destination2)
        print('Files deleted, exiting...')
    else:
        print('No files deleted, aborting...')
        exit()


if __name__ == "__main__":
    main()