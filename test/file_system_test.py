import unittest

#Se importan los modulos que se quieren añadir al TestSuit
import test.get_files_test as test_get_files
import test.get_directories_test as test_get_directories
import test.create_remove_dir_file_test as test_create_remove_dir


#Se inicializa el TestSuite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

#Se añaden los Test de los modulos importados
suite.addTests(loader.loadTestsFromModule(test_get_files))
suite.addTests(loader.loadTestsFromModule(test_get_directories))
suite.addTests(loader.loadTestsFromModule(test_create_remove_dir))

#Se inicializa el runner, se le pasa el TestSuite que se quiere ejecutar y se ejecuta
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)