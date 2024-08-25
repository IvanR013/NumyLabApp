from Helpers import *
from defcalculos import *
from graficar import mostrar_grafico


def opcion_seleccionada(app):
   
    app.limpiar_dinamico_frame()
   
    opcion_var = app.get_opcion_var()
   
    seleccion = opcion_var.get()

    if seleccion in ["Operaciones aritméticas (+ - * /)", "Derivación", "Integración Indefinida", "Gráficos (sólo funciones con x)"]:
       
        textoUser = mostrar_entry(app.get_dinamico_frame())
        boton_calcular,  button_frame = boton_check(app.get_dinamico_frame(), app)
        
        if seleccion == "Derivación":
         
            boton_calcular.config(command=lambda: calcular_derivada(textoUser, app))
       
        elif seleccion == "Integración Indefinida":
          
            boton_calcular.config(command=lambda: calcular_integracion(textoUser, app))        
      
        elif seleccion == "Operaciones aritméticas (+ - * /)":
         
            boton_calcular.config(command=lambda: calcular_suma(textoUser, app))        
      
        elif seleccion == "Operaciones aritméticas (+ - * /)":
          
            boton_calcular.config(command=lambda: calcular_resta(textoUser, app))        
       
        elif seleccion == "Operaciones aritméticas (+ - * /)":
           
            boton_calcular.config(command=lambda: calcular_multiplicacion(textoUser, app))        
        
        elif seleccion == "Operaciones aritméticas (+ - * /)":
           
            boton_calcular.config(command=lambda: calcular_division(textoUser, app))        

        elif seleccion == "Gráficos (sólo funciones con x)":
             
            boton_calcular.config(command=lambda: mostrar_grafico(textoUser.get(), 'x', app))
            
        
    app.opcion_anterior = seleccion




def calcular_derivada(textoUser, app):
    try:
       
        funcion_string = preprocesar_funcion(textoUser.get()) 
       
        funcion = sp.sympify(funcion_string)  
        
        
        derivada = sp.diff(funcion, sp.Symbol('x'))
        
        resultado_calculo(app.get_dinamico_frame(), app, derivada)
    
    except Exception as e:
    
        resultado_calculo(app.get_dinamico_frame(), app, f"Error: {str(e)}")



def calcular_integracion(textoUser, app):
   
    try:
        
        funcion_string = preprocesar_funcion(textoUser.get())
        
        
        funcion = sp.sympify(funcion_string)
        
        
        integracion = sp.integrate(funcion, sp.Symbol('x'))
        
        
        resultado_final = f"{integracion} + C"
        
        
        resultado_calculo(app.get_dinamico_frame(), app, resultado_final)
    
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
        expresion = preprocesar_funcion(textoUser.get())  
    
        resultado = evaluar_expresion(expresion)
    
        resultado_calculo(app.get_dinamico_frame(), app, resultado)
   
    except Exception as e:
   
        resultado_calculo(app.get_dinamico_frame(), app, f"Error: {str(e)}")



def calcular_division(textoUser, app):

    try:
        expresion = preprocesar_funcion(textoUser.get())  
   
        resultado = evaluar_expresion(expresion)
   
        resultado_calculo(app.get_dinamico_frame(), app, resultado)
   
    except Exception as e:
   
        resultado_calculo(app.get_dinamico_frame(), app, f"Error: {str(e)}")



def calcular_multiplicacion(textoUser, app):

    try:
   
        expresion = preprocesar_funcion(textoUser.get()) 
   
        resultado = evaluar_expresion(expresion)
   
        resultado_calculo(app.get_dinamico_frame(), app, resultado)
   
    except Exception as e:
   
        resultado_calculo(app.get_dinamico_frame(), app, f"Error: {str(e)}")
        


