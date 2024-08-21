import tkinter as tk
from funciones import opcion_seleccionada

class App:

    def __init__(self, GUI):

        self.GUI = GUI
        self.frame = tk.Frame(self.GUI)
        self.frame.pack(expand=True, fill='both')

        # Widgets fijos
        self.bienvenida = tk.Label(self.frame, text="NumyLab - Versión DEMO Fase INDEV")
        self.bienvenida.pack(side="top", pady=10, anchor='n')
        self.mensaje_menu = tk.Label(self.frame, text="Introducí La operación a calcular:")
        self.mensaje_menu.pack()

        # Frame para opciones
        self.opciones_frame = tk.Frame(self.frame)
        self.opciones_frame.pack(pady=10, padx=10, fill='x')

        # Frame para widgets dinámicos
        
        self.dinamico_frame = tk.Frame(self.frame)
        self.dinamico_frame.pack(pady=10, padx=10,  fill='both')

        # Menú de opciones
        
        self.opcion_var = tk.StringVar(self.frame)
        self.opcion_var.set("Selecciona una operación")
        opciones = ["Suma", "Resta", "Division", "Multiplicacion", "Derivación", "Integración", "graficos (sólo funciones)"]
        self.opciones_menu = tk.OptionMenu(self.opciones_frame, self.opcion_var, *opciones)
        self.opciones_menu.pack(pady=10, padx=10, fill='x')

        self.opcion_anterior = None
        self.opcion_var.trace_add("write", lambda name, index, operation: opcion_seleccionada(self))

        # Mensaje de propiedad que va abajo
        
        self.property = tk.Label(GUI, text="Mensaje de propiedad")
        self.property.pack(side="bottom", pady=10, anchor='s')



    def limpiar_dinamico_frame(self):
        
        for widget in self.dinamico_frame.winfo_children():
        
            widget.destroy()



    def get_opcion_var(self):
        
        return self.opcion_var



    def get_dinamico_frame(self):
        
        return self.dinamico_frame



def main():
    GUI = tk.Tk()
    GUI.title("NumyLab - DEMO")
    GUI.geometry("400x300")

    app = App(GUI)
    GUI.mainloop()

if __name__ == "__main__":
    main()
