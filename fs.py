from pathlib import Path
from typing import List, Union, Dict
from os import mkdir
from os.path import join

class FileSystemItem:

    __path: Path
    __name: str
    __extension: str
    __is_hidden: bool

    def __init__(self, path: Path):
        if not path.is_file():
            raise FsException(msg="FileSystemItem only can be initialized with path of type 'files'")
        
        self.__path = path
        
        # Get name without extension
        dot_ext = path.name.rfind(".")

        self.__is_hidden = False

        # Is a hidden file, so don't has extension
        if dot_ext == 0 or dot_ext == -1:
            if dot_ext == 0:
                self.__is_hidden = True
            self.__name = path.name
            self.__extension = ""

        else:
            self.__name = path.name[:dot_ext]
            self.__extension = path.name[dot_ext + 1:]


    @property
    def path(self) -> Path:
        return self.__path

    @property
    def absolute(self) -> Path:
        return self.__path.absolute()

    @property
    def parent(self) -> Path:
        return self.__path.parent

    @property
    def name(self) -> str:
        return self.__name

    @property
    def name_ext(self) -> str:
        if self.__extension == "":
            return self.name
        else:
            return f"{self.__name}.{self.__extension}"

    @property
    def extension(self) -> str:
        return self.__extension

    def is_hidden(self) -> bool:
        return self.__is_hidden

    def __repr__(self):
        return str(self)

    def __str__(self) -> str:
        if self.__is_hidden:
            return self.__name
        else:
            return self.name_ext


class FsException(Exception):

    def __init__(self, msg: str):
        super().__init__(msg)

def __is_folder_structure(path: Path):
    return str(path).find("/") >= 0

def __strpath_to_pathobject(path) -> Path:
    """
    Converts the path string into Path object, if the path is already an instance
    of Path the function will do nothing.

    If the given 'path' is not a correct path an error will be raised.
    """
    if type(path) == str:
        p = Path(path)
        if p.exists():
            return p
        else:
            raise FsException(msg=f"Path not exists: {p}")

    elif isinstance(path, Path):
        if path.exists():
            return path
        else:
            raise FsException(msg=f"Path not exists: {path}")
    
    else:
        raise FsException(msg=f"Path must be an instance of str or Path object (from pathlib), but got: {type(path)}")


def get_files(path: Union[str, Path] = Path("./"), files_extensions: List[str]=[], hidden_files: bool = False) -> List[FileSystemItem]:
    path = __strpath_to_pathobject(path)
    
    files = list()

    for element in path.iterdir():
        if not element.is_file(): continue

        fs_item = FileSystemItem(element)

        if not hidden_files and fs_item.is_hidden(): continue

        # Just put all the files items found in the path
        if len(files_extensions) == 0:
            files.append(fs_item)

        else:
            if fs_item.extension in files_extensions:
                files.append(fs_item)

    return files

def get_directories(path: Union[str, Path] = Path("./")) -> List[Path]:
    path = __strpath_to_pathobject(path)
    return [x for x in path.iterdir() if x.is_dir()]


def create_dir(name: str, path: Union[str, Path] = Path("./")):
    """
    Creates a new directory if not exist yet, otherwise this function don't have any affects

    Parameters:
    -----------
    - name: str -> name of the new directory
    - path: str -> path where to create the new directory, default value use current path
    """
    path = __strpath_to_pathobject(path)

    directories = get_directories(path)
    directories = [directory.name for directory in directories]

    if name not in directories:
        mkdir(join(path, name))


def __create_recursive_dirs(dir_structure: Path, path: Path):
    dirs = dir_structure.as_posix().split("/")
    if dirs[-1] == "": dirs = dirs[:-1]

    for d in dirs:
        create_dir(d, path)
        path = Path(path, Path(d))    

def create_folder_structure(structure: Dict[Union[Path, str], List[Union[Path, str]]]):
    for path, items in structure.items():
        path = path
        for item in items:
            if __is_folder_structure(item):
                __create_recursive_dirs(Path(item), path)
            else:
                create_dir(item, path)




if __name__ == "__main__":
    files = get_files()
    print(files)
    print(get_directories())

    for f in files:
        print("Name: ", f.name_ext)

    folders = {

        "./" : [
            "dataset/info/train_info",
        ],

        "dataset" : ["images", "train", "test", "sergio/culero/malo"]
    }

    create_folder_structure(folders)
    
