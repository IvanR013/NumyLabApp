'''
Numylab V1.0 - Desarrollada por Ivan Rodriguez, Aplicación sin firma digital aún.

'''

import tkinter as tk
from funciones import opcion_seleccionada

class App:
    
    '''
    :Documentación en Español: 
    
    Generación de la interfaz gráfica con Tkinter hecha encapsulada en esta clase para mayor escalabilidad si se llegara a actualizar.
    
    
    :English Docs:
    
    GUI development in this class to get easier to update in that case.
    
    '''

    def __init__(self, GUI):
        
        '''
        Método constructor para inicializar la interfaz gráfica de la aplicación.

        :GUI: La ventana principal de la aplicación, que es una instancia de Tkinter.
    
        Este constructor configura la ventana principal de la aplicación, 
        crea un marco (frame) para organizar los widgets y añade varios 
        elementos de la interfaz gráfica, incluyendo etiquetas y menús. 
        Se establece un fondo de color específico y se configura un menú 
        de opciones para seleccionar distintas operaciones matemáticas.

        :Widgets creados:
       
        - Bienvenida: Etiqueta que muestra el título de la aplicación.
        - Mensaje de menú: Etiqueta que indica al usuario que introduzca la operación a calcular.
        - Frame para opciones: Contenedor para el menú de selección de operaciones.
        - Frame dinámico: Contenedor para widgets que se agregarán dinámicamente.
        - Menú de opciones: Menú desplegable que permite al usuario seleccionar entre varias operaciones.
        - Mensaje de propiedad: Etiqueta que muestra el nombre del desarrollador al pie de la ventana (el mío 🤝).
        
        :English Docs:
        
        This Constructor Method sets up the app's main window. 
        It begin's by creating a frame to organize many widgets in it, 
        including different tags and menus. A specific background color is applied
        and a option menu is provided to select any enabled mathematical operation.
        
        :Created Widgets:
        
        - Welcome: Tag that prints in window the app's brand or tittle.
        - Menu message: Tag that generates a message to instruct user to enter any selected operation.
        - Option Frame: Container with the operation menu selector.
        - Dynamic Frame: Container to widgets dynamically added.
        - Option menu: Dropdown menu that allows the user to select between various operations.
        - Property Message: Label at the bottom  to show the developer's name (mine  🤝).   
        '''

    def __init__(self, GUI):

        self.GUI = GUI
        # self.GUI.iconbitmap('assets/n.ico')
        self.frame = tk.Frame(self.GUI, bg= '#1C646D')
        self.frame.pack(expand=True, fill='both')

        # Widgets fijos
        self.bienvenida = tk.Label(self.frame, bg='#1C646D', font=('Arial', 12), fg='white', text="- NumyLab - Calculadora y graficadora -")
        self.bienvenida.pack(side="top", pady=10, anchor='n')
        self.mensaje_menu = tk.Label(self.frame, bg='#1C646D', font=('Arial', 12),fg='white', text="Introducí La operación a calcular:")
        self.mensaje_menu.pack()

        # Frame para opciones
        self.opciones_frame = tk.Frame(self.frame, bg= '#1C646D')
        self.opciones_frame.pack(pady=10, padx=10, fill='x')

        # Frame para widgets dinámicos
        
        self.dinamico_frame = tk.Frame(self.frame, bg='#1C646D')
        self.dinamico_frame.pack(pady=10, padx=10,  fill='both')

        # Menú de opciones
        
        self.opcion_var = tk.StringVar(self.frame)
        self.opcion_var.set("Selecciona una operación")
        opciones = ["Operaciones aritméticas (+ - * /)", "Derivación", "Integración Indefinida", "Gráficos (sólo funciones con x)"]
        self.opciones_menu = tk.OptionMenu(self.opciones_frame, self.opcion_var, *opciones)
        self.opciones_menu.pack(pady=10, padx=10, fill='x')

        self.opcion_anterior = None
        self.opcion_var.trace_add("write", lambda name, index, operation: opcion_seleccionada(self))

        # Mensaje de propiedad que va abajo
        
        self.property = tk.Label(GUI, font=('Arial', 11) ,text="Desarrollado por IvanR013")
        self.property.pack(side="bottom", pady=10, anchor='s')



    def limpiar_dinamico_frame(self):
        
        '''
        El frame dinámico es el input donde se introduce el texto.
        
        Este método itera sobre el y lo resetea para borrar el contenido.
        '''
        
        for widget in self.dinamico_frame.winfo_children():
        
            widget.destroy()



    def get_opcion_var(self):
        
        '''
        Genera el menú desplegable.
        '''
        
        return self.opcion_var



    def get_dinamico_frame(self):
        '''
        Hace aparecer el input de operaciones.
        '''
        
        return self.dinamico_frame



def main():
    
    GUI = tk.Tk()
    GUI.title("NumyLab V1.0")
    GUI.geometry("400x300")

    app = App(GUI)
    
    GUI.mainloop() # Instancia de APP

if __name__ == "__main__":
    
    GUI.mainloop()

if __name__ == "__main__":
    main()