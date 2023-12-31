
import dataStructures.observatorPattern as Obs
import tkinter as tk
from tkinter import filedialog


class GUI( Obs.ObservableSubject ): #hereda de la clase indicada para poder usar el aptron

    #constructor del objeto
    def __init__(self, nombre):
        self.nombre = nombre
        self.observators = []
        self.observables = []
        self.archiveRuteIn = ""
        self.archiveRuteOut = ""
        print("se creo el observable")

        # Crear la ventana principal
        self.root = tk.Tk()
        self.root.title("Pseudo-Ensamblador")

        # Crear un ventana de texto para mostrar el contenido (izquierda)
        self.text_widget = tk.Text(self.root, wrap="word",background="lavender", width=65, height=40, state=tk.DISABLED)
        self.text_widget.pack(side=tk.LEFT, padx=10, pady=10,expand=True, fill=tk.BOTH)

        # Crear botones para cargar y guardar archivos (izquierda)
        self.load_button = tk.Button(self.root, text="Cargar Archivo", command=self.cargar_archivo )
        self.load_button.pack(side=tk.LEFT, pady=5)

        self.save_button = tk.Button(self.root, text="Guardar Archivo", command=self.guardar_archivo )
        self.save_button.pack(side=tk.LEFT, pady=5)

        # Crear una etiqueta para mostrar el estado de la operación (izquierda)
        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack(side=tk.LEFT, pady=5)

        # Crear un widget de texto para mostrar el contenido (derecha)
        self.text_widget_derecha = tk.Text(self.root, wrap="word", background="LightCyan", width=65, height=40, state=tk.DISABLED)
        self.text_widget_derecha.pack(side=tk.RIGHT, padx=10, pady=10,expand=True, fill=tk.BOTH)

        # Crear botón para cargar archivo en la caja de texto derecha
        self.load_button_derecha = tk.Button(self.root, text="Cargar Archivo traducido", command=self.cargar_archivo_derecha )
        self.load_button_derecha.pack(side=tk.RIGHT, pady=5)

    def mainLoop(self):
        # Iniciar el bucle principal de la aplicación
        self.root.mainloop()

    def cargar_archivo(self):
        self.archiveRuteIn = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos de texto", "*.txt")])
        if self.archiveRuteIn:
            with open(self.archiveRuteIn, 'r') as file:
                contenido = file.read()
                self.text_widget.config(state=tk.NORMAL)
                self.text_widget.delete(1.0, tk.END)  # Borrar contenido actual
                self.text_widget.insert(tk.END, contenido)
                self.text_widget.config(state=tk.DISABLED)

                #self.notifyObs( "load_leftArchive", self.archiveRuteIn )

    def cargar_archivo_derecha(self):
        self.archiveRuteOut = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos de texto", "*.txt")])
        if self.archiveRuteOut:
            with open(self.archiveRuteOut, 'r') as file:
                contenido = file.read()
                self.text_widget_derecha.config(state=tk.NORMAL)
                self.text_widget_derecha.delete(1.0, tk.END)  # Borrar contenido actual
                self.text_widget_derecha.insert(tk.END, contenido)
                self.text_widget_derecha.config(state=tk.DISABLED)

                #self.notifyObs( "load_rightArchive", self.archiveRuteOut )

    def guardar_archivo(self):
        
        self.archiveRuteOut = filedialog.asksaveasfilename(title="Guardar como", filetypes=[("Archivos de texto", "*.txt")])
        if self.archiveRuteIn:

            self.notifyObs( "saveTranslated", self.archiveRuteIn, self.archiveRuteOut )
            self.status_label.config(text="Archivo guardado correctamente.")

""" seccion de creacion de objetos """

UserInterface = GUI( "Pseudo-NASM" )