# CRUD-python-tkinter

Para ejecutar el codigo solo se necesita abrir el .exe

El archivo .exe se creó con pyinstaller:

1. Guardar el archivo bbdd.py en una carpeta
2. Abrir CMD y e ir a la ruta donde esta esa carpeta
3. ejecutar el siguiente comando: pyinstaller --windowed --onefile bbdd.py

-- windowed sirve para que cuando se abre el .exe no se abra tambien el cmd
-- onefile con este modificador logras que el .exe no necesite de una carpeta con archivos sino que puedes mover el ejecutable a cualquier carpeta u ordenador y funcionara ya que guarda todo dentro del mismo
Si quieres agregarle un icono deberas tener un archivo de imagen .ico en la misma carpeta que el archivo .py con el codigo y agregarle el siguiente modificador al comando del cmd: --icon= 
Entonces quedaria asi: pyinstaller --windowed --onefile --icon=./tulogo.ico bbdd.py

Con el './' indicamos que el archivo ico se encuentra en la misma carpeta
