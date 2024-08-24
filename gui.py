import tkinter as tk
from funciones import opcion_seleccionada

class App:

    def __init__(self, GUI):

        self.GUI = GUI
        self.GUI.iconbitmap('assets/icconn.ico')
        self.frame = tk.Frame(self.GUI, bg= 'lightblue')
        self.frame.pack(expand=True, fill='both')

        # Widgets fijos
        self.bienvenida = tk.Label(self.frame, bg='lightblue', font=('Sans', 12), text="NumyLab - Fase Beta")
        self.bienvenida.pack(side="top", pady=10, anchor='n')
        self.mensaje_menu = tk.Label(self.frame, bg='lightblue', font=('Sans', 12), text="Introducí La operación a calcular:")
        self.mensaje_menu.pack()

        # Frame para opciones
        self.opciones_frame = tk.Frame(self.frame, bg= 'lightblue')
        self.opciones_frame.pack(pady=10, padx=10, fill='x')

        # Frame para widgets dinámicos
        
        self.dinamico_frame = tk.Frame(self.frame, bg='lightblue')
        self.dinamico_frame.pack(pady=10, padx=10,  fill='both')

        # Menú de opciones
        
        self.opcion_var = tk.StringVar(self.frame)
        self.opcion_var.set("Selecciona una operación")
        opciones = ["Operaciones aritméticas (+ - * /)", "Derivación", "Integración Indefinida", "graficos (sólo funciones)"]
        self.opciones_menu = tk.OptionMenu(self.opciones_frame, self.opcion_var, *opciones)
        self.opciones_menu.pack(pady=10, padx=10, fill='x')

        self.opcion_anterior = None
        self.opcion_var.trace_add("write", lambda name, index, operation: opcion_seleccionada(self))

        # Mensaje de propiedad que va abajo
        
        self.property = tk.Label(GUI, font=('Sans', 11) ,text="Desarrollado por IvanR013")
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
    GUI.title("NumyLab - Beta")
    GUI.geometry("400x300")

    app = App(GUI)
    GUI.mainloop()

if __name__ == "__main__":
    main()