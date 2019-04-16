import sys
import os

def listFiles(destination1, destination2):

  destination1Photos = os.listdir(destination1)
  destination2Photos = os.listdir(destination2)

  dupeFiles = []

  for photo in destination1Photos:
    if(photo in destination2Photos):
      dupeFiles.append(photo)
  
  if(len(dupeFiles) is 0):
    print('No dupe files found!')
    exit()
 
  val = input(str(len(dupeFiles)) + ' duplicate images found. Enter \'y\' to delete or  \'n\' to abort:\n')

  if(val == 'y'):
    for dupeFile in dupeFiles:
      os.remove(destination1 + '\\' + dupeFile)
      os.remove(destination2 + '\\' + dupeFile)
  else:
    print('No files deleted, aborting...')
    exit()

if __name__ == "__main__":
  listFiles(sys.argv[1], sys.argv[2])