# Creado por Wayner Castillo
# github: https://github.com/cybersecrd

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import os

class PyToExeConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Compilador Python a EXE")
        self.root.geometry("600x450")
        
        # Variables para almacenar las rutas
        self.script_path = tk.StringVar()
        self.icon_path = tk.StringVar()
        self.output_name = tk.StringVar(value="MiAplicacion")
        self.output_path = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Configurar el estilo para mejor apariencia
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 9))
        style.configure('TEntry', font=('Arial', 9))
        
        # Título
        title_label = ttk.Label(self.root, text="Compilador Python a EXE", 
                               font=('Arial', 16, 'bold'))
        title_label.pack(pady=20)
        
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(padx=20, pady=10, fill='both', expand=True)
        
        # Seleccionar archivo Python
        ttk.Label(main_frame, text="Archivo Python (.py):").grid(row=0, column=0, sticky='w', pady=5)
        ttk.Entry(main_frame, textvariable=self.script_path, width=50).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(main_frame, text="Examinar", command=self.browse_script).grid(row=0, column=2, padx=5, pady=5)
        
        # Seleccionar icono
        ttk.Label(main_frame, text="Icono (.ico) - Opcional:").grid(row=1, column=0, sticky='w', pady=5)
        ttk.Entry(main_frame, textvariable=self.icon_path, width=50).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(main_frame, text="Examinar", command=self.browse_icon).grid(row=1, column=2, padx=5, pady=5)
        
        # Nombre del aplicativo
        ttk.Label(main_frame, text="Nombre del ejecutable:").grid(row=2, column=0, sticky='w', pady=5)
        ttk.Entry(main_frame, textvariable=self.output_name, width=50).grid(row=2, column=1, padx=5, pady=5)
        
        # Ruta de guardado
        ttk.Label(main_frame, text="Carpeta destino:").grid(row=3, column=0, sticky='w', pady=5)
        ttk.Entry(main_frame, textvariable=self.output_path, width=50).grid(row=3, column=1, padx=5, pady=5)
        ttk.Button(main_frame, text="Examinar", command=self.browse_output).grid(row=3, column=2, padx=5, pady=5)
        
        # Checkbox para ventana de consola
        self.console_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(main_frame, text="Mostrar consola (quitar marca para aplicaciones GUI)", 
                       variable=self.console_var).grid(row=4, column=0, columnspan=3, sticky='w', pady=10)
        
        # Checkbox para un solo archivo
        self.onefile_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(main_frame, text="Crear un solo archivo ejecutable", 
                       variable=self.onefile_var).grid(row=5, column=0, columnspan=3, sticky='w', pady=5)
        
        # Barra de progreso
        self.progress = ttk.Progressbar(self.root, mode='indeterminate')
        self.progress.pack(fill='x', padx=20, pady=10)
        
        # Botón de compilación
        compile_btn = ttk.Button(self.root, text="COMPILAR A EXE", 
                                command=self.compile_to_exe, style='Accent.TButton')
        compile_btn.pack(pady=20)
        
        # Configurar columnas
        main_frame.columnconfigure(1, weight=1)
    
    def browse_script(self):
        filename = filedialog.askopenfilename(
            title="Seleccionar archivo Python",
            filetypes=[("Python files", "*.py"), ("All files", "*.*")]
        )
        if filename:
            self.script_path.set(filename)
            # Sugerir nombre por defecto basado en el archivo Python
            base_name = os.path.splitext(os.path.basename(filename))[0]
            self.output_name.set(base_name)
    
    def browse_icon(self):
        filename = filedialog.askopenfilename(
            title="Seleccionar archivo de icono",
            filetypes=[("Icon files", "*.ico"), ("All files", "*.*")]
        )
        if filename:
            self.icon_path.set(filename)
    
    def browse_output(self):
        folder = filedialog.askdirectory(title="Seleccionar carpeta destino")
        if folder:
            self.output_path.set(folder)
    
    def compile_to_exe(self):
        # Validaciones
        if not self.script_path.get():
            messagebox.showerror("Error", "Debes seleccionar un archivo Python para compilar.")
            return
        
        if not self.output_path.get():
            messagebox.showerror("Error", "Debes seleccionar una carpeta destino.")
            return
        
        # Construir comando de PyInstaller :cite[3]:cite[4]:cite[7]
        cmd = ['pyinstaller']
        
        if self.onefile_var.get():
            cmd.append('--onefile')
        
        if not self.console_var.get():
            cmd.append('--windowed')
        
        if self.icon_path.get():
            cmd.extend(['--icon', self.icon_path.get()])
        
        if self.output_name.get():
            cmd.extend(['--name', self.output_name.get()])
        
        if self.output_path.get():
            cmd.extend(['--distpath', self.output_path.get()])
            # También configurar rutas de trabajo y spec en la misma carpeta
            work_path = os.path.join(self.output_path.get(), 'build')
            spec_path = self.output_path.get()
            cmd.extend(['--workpath', work_path])
            cmd.extend(['--specpath', spec_path])
        
        cmd.append(self.script_path.get())
        
        try:
            # Iniciar progreso
            self.progress.start()
            
            # Ejecutar PyInstaller :cite[10]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            # Detener progreso
            self.progress.stop()
            
            messagebox.showinfo("Éxito", 
                              f"¡Compilación completada con éxito!\n"
                              f"El ejecutable se encuentra en: {self.output_path.get()}")
            
        except subprocess.CalledProcessError as e:
            self.progress.stop()
            error_msg = f"Error durante la compilación:\n{e.stderr}"
            messagebox.showerror("Error", error_msg)
        except FileNotFoundError:
            self.progress.stop()
            messagebox.showerror("Error", 
                               "PyInstaller no está instalado. "
                               "Instálalo con: pip install pyinstaller")

if __name__ == "__main__":
    root = tk.Tk()
    app = PyToExeConverter(root)
    root.mainloop()
