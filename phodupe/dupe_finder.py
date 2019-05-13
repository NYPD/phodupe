import os
import pathlib


class DupeFinder:
    """
        Simple utility class for finding and manipulating duplicate files
    """

    @staticmethod
    def getDuplicateFileNames(directory1, directory2, sameExtension = True):
        """
        Return a list of duplicate file names in both directories

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

        directory1Files = os.listdir(directory1Path)
        directory2Files = os.listdir(directory2Path)

        directory1FilesNoExt = {}
        directory2FilesNoExt = {}

        if sameExtension == False:
            for i, file in enumerate(directory1Files):
                purePath = pathlib.Path(directory1 + '/' + file)
                directory1FilesNoExt[purePath.stem] = purePath.suffix
            for i, file in enumerate(directory2Files):
                purePath = pathlib.Path(directory2 + '/' + file)
                directory2FilesNoExt[purePath.stem] = purePath.suffix

        dupeFiles = []

        if sameExtension:
            for file in directory1Files:
                if(file in directory2Files):
                    dupeFiles.append(file)
        else:
            for fileName, ext in directory1FilesNoExt.items():
                if fileName in directory2FilesNoExt:
                    dupeFiles.append(fileName + ext)
        //We need to delete both extensions

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
            os.remove(os.path.join(directory1, file))
            os.remove(os.path.join(directory2, file))
