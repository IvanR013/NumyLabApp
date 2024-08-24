
import tkinter as tk
from defcalculos import preprocesar_funcion
from graficar import mostrar_grafico
import sympy as sp

def boton_check(frame, app):
    button_frame = tk.Frame(frame, bg= 'Lightblue')
    button_frame.pack(pady=5, padx=5)
    
    boton_calcular = tk.Button(button_frame,font=('Sans', 12) ,text="Calcular", width=10, height=2)
    boton_calcular.pack(side='left', padx=10)


    boton_calcular.config(command=lambda: prueba(frame, app))

    return boton_calcular, button_frame



def prueba(frame, app):
    try:
        textoUser = mostrar_entry(frame)
        funcion_string = preprocesar_funcion(textoUser.get())
        funcion = sp.sympify(funcion_string)
        
        if app.get_opcion_var().get() == "Derivación":
        
            resultado = sp.diff(funcion, sp.Symbol('x'))
        
        elif app.get_opcion_var().get() == "Integración":
        
            resultado = sp.integrate(funcion, sp.Symbol('x'))
        
        else:
            resultado = "Operación no soportada para gráficos."


        resultado_calculo(app.get_dinamico_frame(), app, resultado)

    except Exception as e:
      
        resultado_calculo(app.get_dinamico_frame(), app, f"Error: {str(e)}")



def mostrar_entry(frame):
    textoUser = tk.Entry(frame, width=25)
    textoUser.pack(pady=10, padx=10)
   
    return textoUser


def resultado_calculo(button_frame, app, resultado=None): # te muestra el texto del resultado
    
    if hasattr(app, 'resultado_label') and app.resultado_label is not None and app.resultado_label.winfo_exists():
    
        if resultado is not None:
            app.resultado_label.config(text=f"El resultado es: {resultado}")#user
    
    else:
        
        if resultado is not None:
            app.resultado_label = tk.Label(button_frame, bg='lightblue' ,text=f"El resultado es: {resultado}")#user
            app.resultado_label.pack(pady=10)
        
        else:
            
            print("Label existente, pero no se proporcionó un resultado") # debug
