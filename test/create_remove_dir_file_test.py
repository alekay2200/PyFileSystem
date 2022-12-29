from posixpath import join
from fs.fileSystem import create_dir, create_dirs, get_files, remove_dir, get_directories, remove_dir_and_content, remove_dirs, remove_file
import unittest

class TestCreateRemoveDirFile(unittest.TestCase):
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
    def test_create_existing_directories(self):
        dirs_names = ["d1", "d2", "d3", "d4"]

        create_dirs(dirs_names, "test/elements")

        directories = get_directories("test/elements")
        directories.sort()

        self.assertEqual(dirs_names, directories)

        remove_dirs(dirs_names, "test/elements")


    def test_create_non_existing_directories_and_remove_it(self):
        dirs_names = ["d5", "d6", "d7"]
        path = "test/elements"

        create_dirs(dirs_names, path)

        directories = get_directories(path)
        directories.sort()

        for dirname in dirs_names:
            self.assertIn(dirname, directories)

        remove_dirs(dirs_names, path)


    def test_create_non_existing_empty_directory_and_remove_it(self):
        dirname = "non_existing_dir"
        create_dir(dirname)
        directories = get_directories()
        self.assertIn(dirname, directories)
        remove_dir(dirname)

    def test_create_non_existing_directory_and_remove_it(self):
        parent_folder = "parent"
        child_folder = "child"
        file_name = "file.txt"

        create_dir(parent_folder)
        create_dir(child_folder, parent_folder)
        directories = get_directories()
        child_directories = get_directories(parent_folder)

        with open(join(parent_folder, file_name), "w") as f:
            f.write("testing")

        self.assertIn(parent_folder, directories)
        self.assertIn(child_folder, child_directories)

        remove_dir_and_content(parent_folder)

    def test_remove_file_with_extension(self):
        filename = "test.txt"

        with open(filename, "w") as f:
            f.write("testing")

        files = get_files()

        self.assertIn(filename, files)
        remove_file(filename)
        files = get_files()
        self.assertNotIn(filename, files)

    def test_remove_file_without_extension(self):
        filename = "test.txt"
        filename_without_extension = "test"

        with open(filename, "w") as f:
            f.write("testing")

        files = get_files()

        self.assertIn(filename, files)
        remove_file(filename_without_extension)
        files = get_files()
        self.assertNotIn(filename, files)


if __name__ == "__main__":
    # Uncomment to execute single test
    #unittest.main()
    pass