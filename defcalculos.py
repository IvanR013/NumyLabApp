import sympy as sp
import re


def preprocesar_funcion(funcion_string):
    # Reemplaza las operaciones cotidianas por operadores matemáticos válidos para SymPy
    funcion_string = funcion_string.replace('^', '**')
    funcion_string = funcion_string.replace('menos', '-')
    funcion_string = funcion_string.replace('mas', '+')
    funcion_string = funcion_string.replace('por', '*')
    funcion_string = funcion_string.replace('dividido', '/')
    funcion_string = funcion_string.replace('al cuadrado', '**2')
    funcion_string = funcion_string.replace('al cubo', '**3')
    
    # Insertar multiplicación implícita entre un número y una variable, por ejemplo '2x' -> '2*x'
    funcion_string = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', funcion_string)
    
    # Elimina espacios en blanco
    funcion_string = funcion_string.replace(' ', '')
    
    return funcion_string


def Derivación(funcion_string, var):
    try:
      
        funcion_string = preprocesar_funcion(funcion_string)
      
        print(f"Función procesada: {funcion_string}")  # debug
      
        funcion = sp.sympify(funcion_string)
      
        var = sp.Symbol(var)
      
        derivar = sp.diff(funcion, var)
      
        print(f"Derivada calculada: {derivar}")  # debug
      
        return str(derivar)
    
    except Exception as e:
    
        return f"Error en derivación: {str(e)}" # user



def Integración(funcion_string, var):
    try:
        # Preprocesa la función, si es necesario
        funcion_string = preprocesar_funcion(funcion_string)
        
        # Define la variable simbólica para la integración
        var = sp.Symbol(var)
        
        # Convierte la cadena de la función en una expresión simbólica
        funcion = sp.sympify(funcion_string)
        
        # Realiza la integración
        integrar = sp.integrate(funcion, var)
        
        # Añade la constante de integración 'C'
        resultado_con_constante = f"{integrar} + C"
        
        return str(resultado_con_constante)
    
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




def evaluar_expresion(expresion):
   
    try:
       
        
        resultado = eval(expresion) # correccion de eval
   
        return resultado
    
    
    except Exception as e:
   
        return f"Seguro intentaste dividir por cero o algo así."