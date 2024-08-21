import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from defcalculos import preprocesar_funcion


def mostrar_grafico(funcion_string, variable, app):
    try:
       
        funcion_string = preprocesar_funcion(funcion_string)
        func = sp.lambdify(sp.Symbol(variable), sp.sympify(funcion_string), 'numpy')
        x = np.linspace(-10, 10, 400)
        y = func(x)
        
        fig, ax = plt.subplots(figsize=(8, 6))
       
        ax.plot(x, y, label=f'Función: {funcion_string}')
        ax.set_xlabel(variable)
        ax.set_ylabel('Valor')
        ax.set_title('Gráfico de la Función')
        ax.legend()
        ax.grid(True)
        
        plt.show() # grafico en ventana aparte
        
    except Exception as err:
        
        app.get_dinamico_frame(), app, f"Error al graficar, Leete el readme para hacerlo bien." # user
