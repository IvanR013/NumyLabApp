from Helpers import *
from defcalculos import *
from graficar import mostrar_grafico


def opcion_seleccionada(app):
    app.limpiar_dinamico_frame()
    opcion_var = app.get_opcion_var()
    seleccion = opcion_var.get()

    if seleccion in ["Suma", "Resta", "Division", "Multiplicacion", "Derivación", "Integración", "graficos (sólo funciones)"]:
        textoUser = mostrar_entry(app.get_dinamico_frame())
        boton_calcular,  button_frame = boton_check(app.get_dinamico_frame(), app)
        
        if seleccion == "Derivación":
         
            boton_calcular.config(command=lambda: calcular_derivada(textoUser, app))
       
        elif seleccion == "Integración":
          
            boton_calcular.config(command=lambda: calcular_integracion(textoUser, app))        
      
        elif seleccion == "Suma":
         
            boton_calcular.config(command=lambda: calcular_suma(textoUser, app))        
      
        elif seleccion == "Resta":
          
            boton_calcular.config(command=lambda: calcular_resta(textoUser, app))        
       
        elif seleccion == "Multiplicacion":
           
            boton_calcular.config(command=lambda: calcular_multiplicacion(textoUser, app))        
        
        elif seleccion == "Division":
           
            boton_calcular.config(command=lambda: calcular_division(textoUser, app))        

        elif seleccion == "graficos (sólo funciones)":
             
            boton_calcular.config(command=lambda: mostrar_grafico(textoUser.get(), 'x', app))
            
        
    app.opcion_anterior = seleccion



def calcular_derivada(textoUser, app):
    try:
       
        funcion_string = preprocesar_funcion(textoUser.get())  # Preprocesar la función
       
        funcion = sp.sympify(funcion_string)  # Convertir la cadena procesada en una expresión de sympy
        
        # Realizar la derivación respecto a la variable 'x'
        derivada = sp.diff(funcion, sp.Symbol('x'))
        
        resultado_calculo(app.get_dinamico_frame(), app, derivada)
    
    except Exception as e:
    
        resultado_calculo(app.get_dinamico_frame(), app, f"Error: {str(e)}")



def calcular_integracion(textoUser, app):
    try:
        funcion_string = preprocesar_funcion(textoUser.get())  # Preprocesar la función
       
        funcion = sp.sympify(funcion_string)  # Convertir la cadena procesada en una expresión de sympy
        
        # Realizar la integración respecto a la variable 'x'
        integracion = sp.integrate(funcion, sp.Symbol('x'))
        
        resultado_calculo(app.get_dinamico_frame(), app, integracion)
    
    except Exception as e:
    
        resultado_calculo(app.get_dinamico_frame(), app, f"Error: {str(e)}")



def calcular_suma(textoUser, app):
    try:
        expresion = preprocesar_funcion(textoUser.get())  # Preprocesar la expresión
    
        resultado = evaluar_expresion(expresion)
    
        resultado_calculo(app.get_dinamico_frame(), app, resultado)
    
    except Exception as e:
    
        resultado_calculo(app.get_dinamico_frame(), app, f"Error: {str(e)}")



def calcular_resta(textoUser, app):
    try:
        expresion = preprocesar_funcion(textoUser.get())  # Preprocesar la expresión
    
        resultado = evaluar_expresion(expresion)
    
        resultado_calculo(app.get_dinamico_frame(), app, resultado)
   
    except Exception as e:
   
        resultado_calculo(app.get_dinamico_frame(), app, f"Error: {str(e)}")



def calcular_division(textoUser, app):
    try:
        expresion = preprocesar_funcion(textoUser.get())  # Preprocesar la expresión
   
        resultado = evaluar_expresion(expresion)
   
        resultado_calculo(app.get_dinamico_frame(), app, resultado)
   
    except Exception as e:
   
        resultado_calculo(app.get_dinamico_frame(), app, f"Error: {str(e)}")



def calcular_multiplicacion(textoUser, app):
    try:
   
        expresion = preprocesar_funcion(textoUser.get())  # Preprocesar la expresión
   
        resultado = evaluar_expresion(expresion)
   
        resultado_calculo(app.get_dinamico_frame(), app, resultado)
   
    except Exception as e:
   
        resultado_calculo(app.get_dinamico_frame(), app, f"Error: {str(e)}")
