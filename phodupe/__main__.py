import sys
from phodupe.dupe_finder import DupeFinder


def main():

    destination1 = sys.argv[1]
    destinationsToDelete = []

    for destinationToDelete in sys.argv[2:]:
        destinationsToDelete.append(destinationToDelete)

    recursivelySearch = False

    user_input = input("Would you like to recursivley search all the destination directories? 'y' or 'n'\n")

    if user_input == 'y':
        recursivelySearch = True
    
    allDirectoriesMustHaveSameDupes = False

    user_input = input("Must all directories have the same exact file name? 'y' or 'n'\n")

    if user_input == 'y':
        allDirectoriesMustHaveSameDupes = True

    dupe_files = DupeFinder.getDuplicateFileNames(destination1, destinationsToDelete, recursivelySearch, allDirectoriesMustHaveSameDupes)

    if len(dupe_files) is 0:
        print('No dupe files found!')
        exit()

    user_input = input("{} duplicate file names found. Enter 'y' to delete or 'n' to abort:\n".format(len(dupe_files)))
    
    if user_input == 'y':
        destinationsToDelete.append(destination1)
        DupeFinder.deleteFiles(dupe_files, destinationsToDelete, recursivelySearch)
        print('Files deleted, exiting...')
    else:
        print('No files deleted, aborting...')
        exit()


if __name__ == "__main__":
    main()