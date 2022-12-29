from fs.fileSystem import get_files, create_dirs, create_dir, remove_dir_and_content
import unittest
from typing import List
from os.path import join

class TestGetFiles(unittest.TestCase):
    #Para probar los métodos add y remove se va a partir de un conjunto inicial de 5 elementos,
    #los casos que se van a probar son elemento existente y no existente, y de entre estos casos 
    #el primer elemento, un elemento intermedio y el último elemento.

    #Este método se ejecutará antes de cada test, se prepara el conjunto para el test
    def setUp(self):
        create_dir("elements", "test")
        
        # Create files
        for filename in ["f1", "f2.csv", "f3.txt", "f4.tar.zip"]:
            with open(join("test/elements", filename), "wb") as f: pass

    #Este método se ejecutará despues de cada test, se limpiar el conjunto para el siguiente test
    def tearDown(self):
        remove_dir_and_content("elements", "test")


#---------------------------Test add-----------------------------#
    def test_get_files_with_extension(self):
        expected_output: List[str] = ["f1", "f2.csv", "f3.txt", "f4.tar.zip"].sort()
        files: List[str] = get_files("test/elements").sort()

        self.assertEqual(expected_output, files)

    def test_get_files_without_extension(self):
        expected_output: List[str] = ["f1", "f2", "f3", "f4"].sort()
        files: List[str] = get_files("test/elements", extension=False).sort()

        self.assertEqual(expected_output, files)

    def test_get_extension_concrete_files_with_extensions(self):
        txt_expected_output: List[str] = ["f3.txt"]
        csv_expected_output: List[str] = ["f2.csv"]
        tar_zip_expected_output: List[str] = ["f4.tar.zip"]

        txt_files: List[str] = get_files("test/elements", files_extensions=["txt"])
        csv_files: List[str] = get_files("test/elements", files_extensions=["csv"])

        tar_zip_files: List[str] = get_files("test/elements", files_extensions=["tar.zip"])

        self.assertEqual(txt_expected_output, txt_files)
        self.assertEqual(csv_expected_output, csv_files)
        self.assertEqual(tar_zip_expected_output, tar_zip_files)


    def test_get_extension_concrete_files_without_extensions(self):
        txt_expected_output: List[str] = ["f3"]
        csv_expected_output: List[str] = ["f2"]

        txt_files: List[str] = get_files("test/elements", extension=False, files_extensions=["txt"])
        csv_files: List[str] = get_files("test/elements", extension=False, files_extensions=["csv"])

        self.assertEqual(txt_expected_output, txt_files)
        self.assertEqual(csv_expected_output, csv_files)

if __name__ == "__main__":
    #unittest.main()
    pass