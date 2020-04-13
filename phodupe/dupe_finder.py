import os
import pathlib
import glob
import itertools

class DupeFinder:
    """
        Simple utility class for finding and manipulating duplicate files
    """

    @staticmethod
    def getDuplicateFileNames(directory1, destinationsToDelete, recursivelySearch, matchAllDirectories):
        """
        Returns a tuple containing list of duplicate file name "stems" and a count of directories dupe file name "stems"
        were found.
        
        It uses directory1 as the master directory and then recursively or not (if recursivelySearch is True) checking all the destinationsToDelete for
        duplicate file "stems". If matchAllDirectories is set to true, then all destinationsToDelete (and recursive directories if required) 
        must all have the same file name "stem"
        
        ---

        e.g. 1 : 
        
        recursivelySearch = True

        matchAllDirectories = False

        directory1 : [a.png, b.png]
        
        destinationsToDelete : [a.png, b.png, dir1 : [a.png, c.png]]
        
        returns: ([a, b], 3)

        ---

        e.g. 2 : 
        
        recursivelySearch = True

        matchAllDirectories = True

        directory1 : [a.png, b.png]
        
        destinationsToDelete : [a.png, b.png, dir1 : [a.png, c.png]]
        
        returns: ([a], 3)

        ---

        Parameters
        ----------
        directory1 : str

                Path of the first directory

        destinationsToDelete : list or str

                List of paths to multiple directories or singular string path to 1

        recursivelySearch : boolean

                True or False depending if recursively searching is required
        
        Returns
        -------
        
        (list, int):
            
            list

                A list of the duplicate file names between all directories using the first parameter passed in
                as the master directory. If no duplicate files are found, an empty list is returned

            int

                count of directeries dupe file names were found
        """
        directory1Path = pathlib.Path(directory1)
        destinationDirectoryPaths = []

        if type(destinationsToDelete) is list:
            for destination in destinationsToDelete:
                destinationDirectoryPaths.append(pathlib.Path(destination))
        else:
            destinationDirectoryPaths.append(pathlib.Path(destinationsToDelete))

        if recursivelySearch:
            for destinationDir in destinationDirectoryPaths:
                destinationDirectoryPaths.extend([f.path for f in os.scandir(destinationDir) if f.is_dir()])

        directory1FilesNoExt = []
        destinationDirectoriesFilesListNoExt = []

        for file in os.listdir(directory1Path):
            purePath = pathlib.Path(os.path.join(directory1, file))
            directory1FilesNoExt.append(purePath.stem)

        for destinationDir in destinationDirectoryPaths:

            destinationDirectoriesFilesNoExt = []

            for file in os.listdir(destinationDir):
                purePath = pathlib.Path(os.path.join(destinationDir, file))
                destinationDirectoriesFilesNoExt.append(purePath.stem)
            
            destinationDirectoriesFilesListNoExt.append(destinationDirectoriesFilesNoExt)

        dupeFiles = set()
        dupeDirectoryIndexes = set()

        for fileName in directory1FilesNoExt:

            if matchAllDirectories:
                fileCount = 0
                for destinationDirectoryFilesListNoExt in destinationDirectoriesFilesListNoExt:
                    if fileName in destinationDirectoryFilesListNoExt:
                        fileCount += 1

                if fileCount == len(destinationDirectoriesFilesListNoExt):    
                    dupeFiles.add(fileName)
            else:

                for x in range(len(destinationDirectoriesFilesListNoExt) - 1):
                    if fileName in destinationDirectoriesFilesListNoExt[x]:
                        dupeFiles.add(fileName)
                        dupeDirectoryIndexes.add(x)
        
        if matchAllDirectories:
            return (dupeFiles, len(destinationDirectoryPaths) + 1)
        else:
            return (dupeFiles, len(dupeDirectoryIndexes) + 1)

    @staticmethod
    def deleteFiles(fileNames, destinationsToDelete, recursivelySearch=False):
        """
        Deletes the files provided in all directories passed in

        Parameters
        ----------
        fileNames : list

                List of string files names to delete
        destinationsToDelete : list
                List of directory strings to delete
        """
        for file in fileNames:
            
            for destination in destinationsToDelete:

                if recursivelySearch:
                    fileDestination = '{}{}{}.*'.format(destination, '/**/',file)
                else:
                    fileDestination = '{}/{}.*'.format(destination,file)
                
                directoryGlob = glob.glob(fileDestination, recursive=recursivelySearch)

                for filePath in directoryGlob:
                    os.remove(filePath)