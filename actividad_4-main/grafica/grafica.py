import matplotlib.pyplot as plt #Importamos la libreria matplot
import numpy as np #importamos la libreria numpy



def gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion): #tomamos varios argumentos con el propósito de realizar algún tipo de gráfico o visualización que involucra datos teóricos y datos reales de esfuerzo y deformación.
    
    
    plt.figure(figsize=(15, 6)) #Definimos los tamaños de la figura
    plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) #Creamos el grafico con las variables definidas de esfuerzo y deformación
    plt.scatter(	dataRealEsfuerzo, dataRealDeformacion, color='red') #Creamos un grafico de dispersión y especificamos el color rojo
    plt.xlabel('Esfuerzo [kN]') #Definimos el eje x como el esfuerzo en kn
    plt.ylabel('Deformación [mm]') #Definimos el eje y como la deformación en mm
    plt.title('Gráfica 2: teórico versus real [ZOOM]') #Definimos el titulo del grafico 
    plt.xlim(0, x_lim) #Definimos el rango de los valores del esfuerzo
    plt.ylim(0, y_lim) #Definimos el rango de los valores de la deformación
    plt.grid() #Establecemos la cuadricula en el fondo del grafico
    plt.gca().invert_yaxis() #Invertivos los valores del eje y, es decir que lo prensente de manera descendente 
    plt.show() #Pedimos visualizar el gráfico 

def gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model): #Definimos el grafico de predicción 
  plt.figure(figsize=(15, 6)) #Definimos los tamaños de la figura
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) #Definimos las variables del grafico
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red') #Creamos un grafico de dispersión y especificamos el color rojo
  plt.plot(np.linspace(0,1000).reshape(-1,1),model.predict(np.linspace(0,1000).reshape(-1,1)),'m') #Este código se encarga de trazar una línea o curva de predicciones del modelo sobre un rango de valores en el eje x
  plt.scatter(	3000 , prediction, color='green') #Pedimos que nos represente la predicción en color verde
  plt.xlabel('Esfuerzo [kN]') #Definimos el eje x como el esfuerzo en kn
  plt.ylabel('Deformación [mm]') #Definimos el rango de los valores de la deformación
  plt.title('Gráfica 3: Predicción a una carga de 3000 kN') #Definimos el titulo del grafico 
  plt.xlim(0, 3000) #Definimos el rango de los valores del esfuerzo
  plt.ylim(0, 45) #Definimos el rango de los valores de la deformación
  plt.grid() #Establecemos la cuadricula en el fondo del grafico
  plt.gca().invert_yaxis() #Invertivos los valores del eje y, es decir que lo prensente de manera descendente
  plt.show() #Pedimos visualizar el gráfico 

def gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion): #Definimos el grafico de comparación teorico vs real
  plt.figure(figsize=(15, 6)) #Definimos los tamaños de la figura
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) #Definimos las variables del grafico
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red') #Creamos un grafico de dispersión y especificamos el color rojo
  plt.xlabel('Esfuerzo [kN]') #Definimos el eje x como el esfuerzo en kn
  plt.ylabel('Deformación [mm]') #Definimos el rango de los valores de la deformación
  plt.title('Gráfica 1: teórico versus real') #Definimos el titulo del grafico
  plt.grid() #Establecemos la cuadricula en el fondo del grafico
  plt.gca().invert_yaxis() #Invertivos los valores del eje y, es decir que lo prensente de manera descendente
  plt.show() #Pedimos visualizar el gráfico