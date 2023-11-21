import tkinter as tk
from tkinter import filedialog

def cargar_archivo():
    ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos de texto", "*.txt")])
    if ruta_archivo:
        with open(ruta_archivo, 'r') as file:
            contenido = file.read()
            text_widget.config(state=tk.NORMAL)
            text_widget.delete(1.0, tk.END)  # Borrar contenido actual
            text_widget.insert(tk.END, contenido)
            text_widget.config(state=tk.DISABLED)

def cargar_archivo_derecha():
    ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos de texto", "*.txt")])
    if ruta_archivo:
        with open(ruta_archivo, 'r') as file:
            contenido = file.read()
            text_widget_derecha.config(state=tk.NORMAL)
            text_widget_derecha.delete(1.0, tk.END)  # Borrar contenido actual
            text_widget_derecha.insert(tk.END, contenido)
            text_widget_derecha.config(state=tk.DISABLED)

def guardar_archivo():
    ruta_archivo = filedialog.asksaveasfilename(title="Guardar como", filetypes=[("Archivos de texto", "*.txt")])
    if ruta_archivo:
        with open(ruta_archivo, 'w') as file:
            contenido = text_widget.get(1.0, tk.END)
            file.write(contenido)
        status_label.config(text="Archivo guardado correctamente.")

# Crear la ventana principal
root = tk.Tk()
root.title("Ensamblador")

# Crear un ventana de texto para mostrar el contenido (izquierda)
text_widget = tk.Text(root, wrap="word",background="lavender", width=65, height=40, state=tk.DISABLED)
text_widget.pack(side=tk.LEFT, padx=10, pady=10,expand=True, fill=tk.BOTH)

# Crear botones para cargar y guardar archivos (izquierda)
load_button = tk.Button(root, text="Cargar Archivo", command=cargar_archivo)
load_button.pack(side=tk.LEFT, pady=5)

save_button = tk.Button(root, text="Guardar Archivo", command=guardar_archivo)
save_button.pack(side=tk.LEFT, pady=5)

# Crear una etiqueta para mostrar el estado de la operación (izquierda)
status_label = tk.Label(root, text="")
status_label.pack(side=tk.LEFT, pady=5)

# Crear un widget de texto para mostrar el contenido (derecha)
text_widget_derecha = tk.Text(root, wrap="word", background="LightCyan", width=65, height=40, state=tk.DISABLED)
text_widget_derecha.pack(side=tk.RIGHT, padx=10, pady=10,expand=True, fill=tk.BOTH)

# Crear botón para cargar archivo en la caja de texto derecha
load_button_derecha = tk.Button(root, text="Cargar Archivo traducido", command=cargar_archivo_derecha)
load_button_derecha.pack(side=tk.RIGHT, pady=5)

# Iniciar el bucle principal de la aplicación
root.mainloop()
