# Compilador_python
Programa para compilar scripts creados con python



🧠 Resumen general

El script crea una interfaz que permite a cualquier usuario:

     Seleccionar un archivo .py.

     Elegir un icono opcional .ico.

    Definir el nombre del ejecutable.

    Elegir la carpeta donde se guardará el .exe.

    Decidir si mostrar la consola o crear un único archivo ejecutable.

    Luego, ejecuta internamente el comando de PyInstaller con los parámetros seleccionados para generar el archivo .exe.

⚙️ Funcionamiento paso a paso

   1- Inicio de la interfaz

     Usa tkinter y ttk para crear una ventana principal titulada "Compilador Python a EXE".

     Define campos y botones para:

    Seleccionar archivo Python.

    Seleccionar ícono.

    Poner nombre de salida.

    Escoger carpeta destino.

    Activar/desactivar consola.

    Crear un solo archivo (--onefile).

2- Selección del archivo .py

    Usa un cuadro de diálogo (filedialog.askopenfilename) para elegir el script Python.

    Automáticamente sugiere el nombre del ejecutable según el archivo elegido.

3- Selección del ícono y carpeta de salida

    Permite buscar un archivo .ico opcional.

    Selecciona la carpeta donde se guardará el .exe.

4- Opciones de compilación

    Checkbox para decidir si el ejecutable mostrará la consola (--windowed o no).

    Checkbox para decidir si crear un solo archivo (--onefile).

5- Compilación

  Cuando el usuario presiona “COMPILAR A EXE”, el programa:

    Valida que haya un script y carpeta seleccionados.

    Construye el comando pyinstaller con las opciones elegidas.

    Ejecuta el comando con subprocess.run().

    Muestra una barra de progreso mientras compila.

    Al finalizar, muestra un mensaje de éxito o error.

Ejemplo del comando que se genera internamente:
pyinstaller --onefile --windowed --icon app.ico --name MiApp --distpath C:\Salida --workpath C:\Salida\build --specpath C:\Salida main.py




6- Manejo de errores
Si falta PyInstaller, muestra un mensaje con la instrucción para instalarlo:

    pip install pyinstaller


Si ocurre un error durante la compilación, muestra la salida del error.




💡 En resumen
Acción	                                       Descripción
Crea una GUI amigable	                         Permite compilar scripts Python sin usar la terminal.
Usa PyInstaller internamente	                 Genera ejecutables .exe desde scripts .py.
Incluye opciones avanzadas	                   Elegir ícono, nombre, destino, consola, un solo archivo.
Ideal para desarrolladores y no técnicos	     Convierte tus programas Python en ejecutables fácilmente.




📦 Requisitos para usarlo

1-Python instalado.

2-PyInstaller instalado (pip install pyinstaller).

3-Tkinter (ya viene con Python).





