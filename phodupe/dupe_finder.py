import os
import pathlib
import glob
import itertools

class DupeFinder:
    """
        Simple utility class for finding and manipulating duplicate files
    """

    @staticmethod
    def getDuplicateFileNames(directory1, destinationsToDelete, recursivelySearch):
        """
        Returns a list of duplicate file name "stems" using directory1 as the
        master directory and then recursively or not (if passed in True) checking all the destinationsToDelete.
        
        e.g. : 
        
        recursivelySearch = True

        directory1 : [a.png, b.png]
        
        destinationsToDelete : [a.png, b.png, dir1 : [a.png, c.png]]
        
        returns: [a, b]

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
        list

            A list of the duplicate file names between all directories using the first parameter passed in
            as the master directory. If no duplicate files are found, an empty list is returned
        """
        directory1Path = pathlib.Path(directory1)

        destinationDirectories = []

        if type(destinationsToDelete) is list:
            for destination in destinationsToDelete:
                destinationDirectories.append(pathlib.Path(destination))
        else:
            destinationDirectories.append(pathlib.Path(destination))

        if recursivelySearch:
            for destinationDir in destinationDirectories:
                destinationDirectories.extend([f.path for f in os.scandir(destinationDir) if f.is_dir()])

        directory1FilesNoExt = []
        destinationDirectoriesFilesNoExt = set()

        for file in os.listdir(directory1Path):
            purePath = pathlib.Path(os.path.join(directory1, file))
            directory1FilesNoExt.append(purePath.stem)

        for destinationDir in destinationDirectories:
            for file in os.listdir(destinationDir):
                purePath = pathlib.Path(os.path.join(destinationDir, file))
                destinationDirectoriesFilesNoExt.add(purePath.stem)

        dupeFiles = []

        for fileName in directory1FilesNoExt:
            if fileName in destinationDirectoriesFilesNoExt:
                dupeFiles.append(fileName)
        
        return dupeFiles

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
                directoryGlob = glob.glob('{}{}{}.*'.format(destination, '/**/',file), recursive=recursivelySearch)
            
                for filePath in directoryGlob:
                    os.remove(filePath)
