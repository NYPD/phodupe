import os


class DupeFinder:
    """
        Simple utility class for finding and manipulating duplicate files
    """

    @staticmethod
    def getDuplicateFileNames(directory1, directory2):
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
        directory1Files = os.listdir(directory1)
        directory2Files = os.listdir(directory2)

        dupeFiles = []

        for file in directory1Files:
            if(file in directory2Files):
                dupeFiles.append(file)

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
            os.remove(directory1 + '\\' + file)
            os.remove(directory2 + '\\' + file)
