from os import listdir, mkdir, getcwd, rmdir, remove
from os.path import isfile, join
from typing import List

def _find_file(file_name: str, files_with_extensions: List[str]):
    '''
    Private function, do not use outside this python file
    find file_name (with or without extension) in a list of files with (with extension)
    '''
    found = None
    extension = file_name.find(".") >= 0

    for n in files_with_extensions:
        if extension:
            if n == file_name:
                found = n
                break 
        else:
            if file_name == n[:n.find(".")]:
                found = n
                break
           
    return found



def get_directories(path: str) -> List[str]:
    '''
    path: str -> path where to find directories, if path == "" then use the current path
    '''

    if path == "":
        path = getcwd()

    elements = listdir(path)
    directories = list()

    for e in elements:
        if not isfile(join(path, e)):
            directories.append(e)

    return directories


def get_files(path: str, extension: bool=True, ignore_files_with_extension: List[str]=[]) -> List[str]:
    '''
    path: str -> path where to find files, if path == "" then use the current path
    extension: bool -> True return a list whit the names and extension, False, return a list only with names
    ignore_files_with_extension: List[str] -> list of extensions to ignore
    '''

    if path == "":
        path = getcwd()

    elements = listdir(path)
    files = list()

    for e in elements:
        if isfile(join(path, e)):
            if e[e.find(".")+1:] in ignore_files_with_extension:
                continue
            if extension:
                files.append(e)
            else:
                files.append(e[:e.find(".")])

    return files

def get_directories_and_files(path: str) -> List[str]:
    '''
    path: str -> path where to find directories and files, if path == "" then use the current path
    '''

    if path == "":
        path = getcwd()

    return listdir(path)

def create_dir(path: str, name: str):
    '''
    Create a new directory if not exist yet
    path: str -> path where to create the new directory, if path == "" then use the current path
    name: str -> name of the new directory
    '''

    if path == "":
        path = getcwd()

    directories = get_directories(path)

    if name not in directories:
        mkdir(join(path, name))

def create_dirs(path: str, names: List[str]):
    '''
    Create directories that not exist yet
    path: str -> path where to create the new directory, if path == "" then use the current path
    names: List[str] -> names of the new directories
    '''

    if path == "":
        path = getcwd()

    directories = get_directories(path)
    names = list(dict.fromkeys(names))  #Remove duplicates names

    for name in names:
        if name not in directories:
            mkdir(join(path, name))

def remove_dir(path: str, dir: str):
    '''
    Remove directory if exist
    path: str -> path where the directory is, if path == "" then use the current path
    dir: str -> name of the directory
    '''

    if path == "":
        path = getcwd()

    directories = get_directories(path)

    if dir in directories:
        rmdir(join(path, dir))

def remove_dirs(path: str, dirs: List[str]):
    '''
    Remove existing directories
    path: str -> path where the directory is, if path == "" then use the current path
    dirs: str -> name of the directories to remove
    '''

    if path == "":
        path = getcwd()

    directories = get_directories(path)
    dirs = list(dict.fromkeys(dirs)) #Remove duplicates

    for dir in dirs:
        if dir in directories:
            rmdir(join(path, dir))

def remove_file(path: str, file_name: str):
    '''
    Remove if exist the file
    path: str -> path where the directory is, if path == "" then use the current path
    file: str -> name of file to remove with or without extension
    '''

    if path == "":
        path = getcwd()

    name_to_remove = _find_file(file_name, get_files(path))

    if name_to_remove != None:
        remove(join(path, name_to_remove))


if __name__ == "__main__":
    pass