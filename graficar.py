import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from defcalculos import preprocesar_funcion


def mostrar_grafico(funcion_string, variable, app):
    

    '''
    Si el usuario selecciona la opción de gráficos (y utiliza x como variable de su función), la grafica y ejecuta la ventana con el gráfico aparte. 
    
    '''
    
    from Helpers import resultado_calculo # Para evitar importacion circular.

    from Helpers import resultado_calculo

    
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
        
        plt.show()  
        
    except Exception as err:
       
        
        resultado_calculo(app.get_dinamico_frame(), app, f"Error al graficar: {str(err)}. Leete el readme para hacerlo bien.")
