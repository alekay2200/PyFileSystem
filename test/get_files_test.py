from src.fileSystem import get_files
import unittest
from typing import List

class TestGetFiles(unittest.TestCase):
    #Para probar los métodos add y remove se va a partir de un conjunto inicial de 5 elementos,
    #los casos que se van a probar son elemento existente y no existente, y de entre estos casos 
    #el primer elemento, un elemento intermedio y el último elemento.

    #Este método se ejecutará antes de cada test, se prepara el conjunto para el test
    def setUp(self):
        pass

    #Este método se ejecutará despues de cada test, se limpiar el conjunto para el siguiente test
    def tearDown(self):
        pass


#---------------------------Test add-----------------------------#
    def test_get_files_with_extension(self):
        expected_output: List[str] = ["f1", "f2.csv", "f3.txt"].sort()
        files: List[str] = get_files("test/elements").sort()

        self.assertEqual(expected_output, files)

    def test_get_files_without_extension(self):
        expected_output: List[str] = ["f1", "f2", "f3"].sort()
        files: List[str] = get_files("test/elements", extension=False).sort()

        self.assertEqual(expected_output, files)

    def test_get_extension_concrete_files_with_extensions(self):
        txt_expected_output: List[str] = ["f3.txt"]
        csv_expected_output: List[str] = ["f2.csv"]

        txt_files: List[str] = get_files("test/elements", files_extensions=["txt"])
        csv_files: List[str] = get_files("test/elements", files_extensions=["csv"])

        self.assertEqual(txt_expected_output, txt_files)
        self.assertEqual(csv_expected_output, csv_files)


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