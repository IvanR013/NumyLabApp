import sympy as sp
import re

def preprocesar_funcion(funcion_string): # Maneja palabras que en el lenguaje cotidiano son operadores.
    
    funcion_string = funcion_string.replace('^', 'elevado a la')
    funcion_string = funcion_string.replace('menos', '-')
    funcion_string = funcion_string.replace('mas', '+')
    funcion_string = funcion_string.replace('por', '*')
    funcion_string = funcion_string.replace('dividido', '/')
    funcion_string = funcion_string.replace('^', '**')
    funcion_string = funcion_string.replace('al cuadrado', '**2')
    funcion_string = funcion_string.replace('al cubo', '**3')
    funcion_string = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', funcion_string)
    funcion_string = funcion_string.replace(' ', '')
    
    return funcion_string

def Derivación(funcion_string, var):
    try:
      
        funcion_string = preprocesar_funcion(funcion_string)
      
        print(f"Función procesada: {funcion_string}")  # Para depuración
      
        funcion = sp.sympify(funcion_string)
      
        var = sp.Symbol(var)
      
        derivar = sp.diff(funcion, var)
      
        print(f"Derivada calculada: {derivar}")  # Para depuración
      
        return str(derivar)
    
    except Exception as e:
    
        return f"Error en derivación: {str(e)}"



def Integración(funcion_string, var):
    try:
        funcion_string = preprocesar_funcion(funcion_string)  
       
        funcion = sp.sympify(funcion_string)
       
        var = sp.Symbol(var)
       
        integrar = sp.integrate(funcion, var)
       
        return str(integrar)
    
    except Exception as e:
    
        return f"Error en integración: {str(e)}"

# Funciones Aritméticas
def Resta(a, b):
   
    return a - b



def Multiplicación(a, b):
   
    return a * b



def Division(a, b):
    
   try: return a / b

   except: 
   
       if b == 0:
   
        return "ERR: Todavía no sabemos cómo dividir por cero :("
       


def Suma(a, b):
   
    return a + b



# Evaluar expresión aritmética
def evaluar_expresion(expresion):
   
    try:
        # Usar eval para evaluar la expresión aritmética
        resultado = eval(expresion)
   
        return resultado
    
    except Exception as e:
   
        return f"Seguro intentaste dividir por cero o algo así."
