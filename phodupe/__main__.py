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

    dupeFileInfoTuple = DupeFinder.getDuplicateFileNames(destination1, destinationsToDelete, recursivelySearch, allDirectoriesMustHaveSameDupes)
    dupe_files = dupeFileInfoTuple[0]
    dupeFileLength = len(dupe_files)

    if dupeFileLength is 0:
        print('No dupe files found!')
        exit()

    user_input = input("{} duplicate file names found across {} directories. Enter 'y' to delete or 'n' to abort:\n".format(dupeFileLength, dupeFileInfoTuple[1]))
    
    if user_input == 'y':
        destinationsToDelete.append(destination1)
        DupeFinder.deleteFiles(dupe_files, destinationsToDelete, recursivelySearch)
        print('Files deleted, exiting...')
    else:
        print('No files deleted, aborting...')
        exit()


if __name__ == "__main__":
    main()