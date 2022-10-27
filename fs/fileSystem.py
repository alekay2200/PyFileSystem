from os import listdir, mkdir, rmdir, remove
from os.path import isfile, join, isdir
from typing import List
from shutil import rmtree, copy

def __find_file(file_name: str, files_with_extensions: List[str]):
    """
    Private function, do not use outside this python file
    find file_name (with or without extension) in a list of files with (with extension)
    """
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

def __is_hidden_element(element_name: str) -> bool:
    """
    Return if a dirname is a hidden folder
    """
    return element_name[0] == "."


def get_directories(path: str = "./", hidden_folders=False) -> List[str]:
    """
    path: str -> path where to find directories, default vale use current path
    """

    elements =  listdir(path)
    directories = list()

    for e in elements:
        if isdir(join(path, e)):
            if not hidden_folders and __is_hidden_element(e):
                continue
            else:
                directories.append(e)

    return directories


def get_files(path: str = "./", extension: bool=True, files_extensions: List[str]=[]) -> List[str]:
    """
    path: str -> path where to find files, default vale use current path
    extension: bool -> True return a list whit the names and extension, False, return a list only with names
    file_extensions: List[str] -> list of extensions of files to get
    """

    elements = listdir(path)
    files = list()

    for e in elements:
        if isfile(join(path, e)):
            op = e[e.find(".")+1:]
            if files_extensions != [] and not e[e.find(".")+1:] in files_extensions:
                continue
            if extension:
                files.append(e)
            else:
                files.append(e[:e.find(".")])

    return files

def create_dir(name: str, path: str = "./"):
    """
    Create a new directory if not exist yet
    path: str -> path where to create the new directory, default value use current path
    name: str -> name of the new directory
    """

    directories = get_directories(path)

    if name not in directories:
        mkdir(join(path, name))

def create_dirs(names: List[str], path: str = "./"):
    """
    Create directories that not exist yet
    path: str -> path where to create the new directory, default value use current path
    names: List[str] -> names of the new directories
    """

    directories = get_directories(path)
    names = list(dict.fromkeys(names))  #Remove duplicates names

    for name in names:
        if name not in directories:
            mkdir(join(path, name))

def remove_dir(dir: str, path: str = "./"):
    """
    Remove directory if exist
    path: str -> path where the directory is, default value use current path
    dir: str -> name of the directory
    """

    directories = get_directories(path)

    if dir in directories:
        rmdir(join(path, dir))

def remove_dir_and_content(dir: str, path: str = "./"):
    """
    Remove directory and its content

    path: str -> path where the directory is, default value use current path
    dir: str -> name of the directory
    """
    
    directories = get_directories(path)

    if dir in directories:
        rmtree(join(path, dir))

def remove_dirs(dirs: List[str], path: str = "./"):
    """
    Remove existing directories
    path: str -> path where the directory is, default value use current path
    dirs: str -> name of the directories to remove
    """

    directories = get_directories(path)
    dirs = list(dict.fromkeys(dirs)) #Remove duplicates

    for dir in dirs:
        if dir in directories:
            rmdir(join(path, dir))

def remove_file(file_name: str, path: str = "./"):
    """
    Remove if exist the file
    path: str -> path where the directory is, default value use current path
    file: str -> name of file to remove with or without extension
    """

    name_to_remove = __find_file(file_name, get_files(path))

    if name_to_remove != None:
        remove(join(path, name_to_remove))
        
def copy_file(file_name: str, src_path: str = "./", dst_path: str = ""):
    """
    Copy if exist the file
    file_name: str -> name of file to copy with or without extension
    src_path: str -> path where the directory is, default value use current path
    dst_path: str -> path of the directory where to copy, if it does not exits, it will be created
    """

    name_to_copy = __find_file(file_name, get_files(src_path))
    create_dir(dst_path,'')

    if name_to_copy != None:
        copy(join(src_path,name_to_copy),dst_path)

if __name__ == "__main__":
    pass
