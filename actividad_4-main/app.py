from data.data import * #Importamos todos los modulos del file data
from BD.baseDatos import * #Impotamos todos los modulos del file base de datos
from sklearn.linear_model import LinearRegression #Importamos especificamente la regresión lineal
from grafica.grafica import * #Importamos todos los modulos del file graficas
import pandas as pd #Importamos geopandas

#Datos del excel
dataTeoricoEsfuerzo, dataTeoricoDeformacion = dataTeorico() #Definimos las variables de los datos del excel 

#Datos de la base de datos y realizamos el modelo
data_list = lecturaDatos() #Definimos la lectura de los datos
data_real = pd.DataFrame(data_list) #se utiliza para convertir los datos contenidos en formato de DataFrame, lo que facilita la manipulación y el análisis de los datos
data_real_fit = data_real #Relacionamos data real fit con data real
X = data_real_fit['Esfuerzo[kN]'].values.reshape(-1, 1) #Definimos la variable x y el rango a evaluar 
y = data_real_fit['Deformacion[mm]'].values.reshape(-1, 1) #Definimos la variable y, tambien el rango a evaluar 
x_lim = data_real['Esfuerzo[kN]'].iloc[-1] #Establecemos el limite de x, se utiliza iloc para acceder al último elemento de una serie de DataFrame
y_lim = data_real['Deformacion[mm]'].iloc[-1] #Establecemos el limite de y, se utiliza iloc para acceder al último elemento de una serie de DataFrame
model = LinearRegression() #Indicamos que el modelo es una regreción lineal
model.fit(X, y) #Indicamos las variables del modelo
prediction = round(model.predict(np.array([3000]).reshape(-1, 1))[0][0],1) #Establecemos la predicción en 3000 
print('la predicción a 1000 kN es de: ', prediction ,'mm') #Imprimimos el valor de la predicción en kn


dataRealEsfuerzo = data_real['Esfuerzo[kN]'] #Definimos las variable esfuerzo
dataRealDeformacion = data_real['Deformacion[mm]'] #Definimos la variable deformación

#realizamos la lectura de las gráficas
gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion) #Selecconamos los tres graficos respectivos que se generaron
gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion) #Grafico de predicción
gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model)#grafico de predicción 3000

