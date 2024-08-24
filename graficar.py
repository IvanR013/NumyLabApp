import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from defcalculos import preprocesar_funcion


def mostrar_grafico(funcion_string, variable, app):
    from Helpers import resultado_calculo
    try:
        # Preprocesar la función ingresada por el usuario
        funcion_string = preprocesar_funcion(funcion_string)
        
        # Convertir la función a una función utilizable por numpy
        func = sp.lambdify(sp.Symbol(variable), sp.sympify(funcion_string), 'numpy')
        
        # Generar valores de x y calcular y
        x = np.linspace(-10, 10, 400)
        y = func(x)
        
        # Crear el gráfico
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(x, y, label=f'Función: {funcion_string}')
        ax.set_xlabel(variable)
        ax.set_ylabel('Valor')
        ax.set_title('Gráfico de la Función')
        ax.legend()
        ax.grid(True)
        
        plt.show()  # Mostrar el gráfico en una ventana aparte
        
    except Exception as err:
        # Mostrar un mensaje de error en la aplicación
        
        resultado_calculo(app.get_dinamico_frame(), app, f"Error al graficar: {str(err)}. Leete el readme para hacerlo bien.")
