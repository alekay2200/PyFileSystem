from fs.fileSystem import get_directories, create_dir
import unittest
from typing import List

class TestGetDirectories(unittest.TestCase):
    #Para probar los métodos add y remove se va a partir de un conjunto inicial de 5 elementos,
    #los casos que se van a probar son elemento existente y no existente, y de entre estos casos 
    #el primer elemento, un elemento intermedio y el último elemento.

    #Este método se ejecutará antes de cada test, se prepara el conjunto para el test
    def setUp(self):
        create_dir("elements", "test")


    #Este método se ejecutará despues de cada test, se limpiar el conjunto para el siguiente test
    def tearDown(self):
        pass


#---------------------------Test add-----------------------------#
    def test_get_directories_from_current_folder_without_hidden_folders(self):
        expected_output: List[str] = ["fs", "test"]
        directories: List[str] = get_directories()
        directories.sort()

        self.assertEqual(expected_output, directories)

    def test_get_directories_from_current_folder_with_hidden_folders(self):
        expected_output: List[str] = [".git", "fs", "test"]
        directories: List[str] = get_directories(hidden_folders=True)
        directories.sort()

        self.assertEqual(expected_output, directories)

if __name__ == "__main__":
    #unittest.main()
    pass