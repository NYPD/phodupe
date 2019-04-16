import sys
import os
from dupe_finder import DupeFinder

def main(destination1, destination2):

  dupeFiles = DupeFinder.getDuplicateFileNames(destination1, destination2)
  
  if(len(dupeFiles) is 0):
    print('No dupe files found!')
    exit()
 
  userInput = input(str(len(dupeFiles)) + ' duplicate images found. Enter \'y\' to delete or \'n\' to abort:\n')

  if(userInput == 'y'):
    DupeFinder.deleteFiles(dupeFiles, destination1, destination2)
    print('Files deleted, exiting...')
  else:
    print('No files deleted, aborting...')
    exit()

if __name__ == "__main__":
  main(sys.argv[1], sys.argv[2])