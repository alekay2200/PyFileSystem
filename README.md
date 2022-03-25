# FileSystem

Proporciona una serie de funciones útiles para manejar el sistema de ficheros (en principio solo esta probado para linux, pero seguramente también funcione en máquinas con otros sistemas operativos).

Cada función cuenta con una breve descripción de su funcionamiento junto con descripción y tipo de los parámetros.


# Test
El test principal se encuentra en la ruta ***"/test/file_system_test.py***, este fichero es el encargado de ejecutar todos los test desarrollados.

Tambien se pueden ejecutar cada uno de los test concretos, son cada uno de los ficheros ***_test.py*** de la carpeta test.

# Como ejecutar las pruebas
- Instalar herramienta coverage -> ***pip install coverage***
- Posicionarse en la carpeta root del proyecto
- Ejecutar -> ***coverage run -m test.file_system_test***

## Para generar web con los resultados
- Posicionarse en la carpeta root del proyecto
- Ejecutar -> ***coverage html***