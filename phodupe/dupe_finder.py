import os
import pathlib
import glob
import itertools

class DupeFinder:
    """
        Simple utility class for finding and manipulating duplicate files
    """

    @staticmethod
    def getDuplicateFileNames(directory1, directory2):
        """
        Return a list of duplicate file name "stems" in both directories.
        
        e.g. : 
        
        directory1 : [a.png, b.png]
        
        directory2 : [a.png, b.png]
        
        returns: [a, b]

        Parameters
        ----------
        directory1 : str
            Path of the first directory
        directory2 : str
            Path of the second directory
        
        Returns
        -------
        list
            A list of the duplicate file names between both directories. If no
            duplicate files are found, an empty list is returned
        """
        directory1Path = pathlib.Path(directory1)
        directory2Path = pathlib.Path(directory2)

        directory1FilesNoExt = []
        directory2FilesNoExt = []

        for file in os.listdir(directory1Path):
            purePath = pathlib.Path(os.path.join(directory1, file))
            directory1FilesNoExt.append(purePath.stem)
        for file in os.listdir(directory2Path):
            purePath = pathlib.Path(os.path.join(directory2, file))
            directory2FilesNoExt.append(purePath.stem)

        dupeFiles = []

        for fileName in directory1FilesNoExt:
            if fileName in directory2FilesNoExt:
                dupeFiles.append(fileName)
        
        return dupeFiles

    @staticmethod
    def deleteFiles(fileNames, directory1, directory2):
        """
        Deletes the files provided in both directories

        Parameters
        ----------
        fileNames : list
            List of string files names to delete
        directory1 : str
            Path of the first directory
        directory2 : str
            Path of the second directory
        """
        for file in fileNames:
            
            directory1Path = os.path.join(directory1, file)
            directory2Path = os.path.join(directory2, file)
            
            directory1Glob = glob.glob('{}.*'.format(directory1Path))
            directory2Glob = glob.glob('{}.*'.format(directory2Path))
            
            for filePath in itertools.chain(directory1Glob, directory2Glob):
                os.remove(filePath)
