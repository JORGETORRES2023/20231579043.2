import pandas as pd #Importamos la libreria pandas

# Importar datos del csv
data_teorico = pd.read_csv("D:\Material Universidad\INGENIERÍA\OCTAVO SEMESTRE\PROGRAMACIÓN 2\ACTIVIDAD 4\Data ingeniero 1.csv") #Obtenemos el acceso de la base de datos y la importamos
#Código general
""" En caso que se exigiera realizar la limpieza de la data se haría aca"""

def dataTeorico(): #Definimos los datos teoricos 
    dataTeoricoEsfuerzo = data_teorico['Esfuerzo[kN]'] #Establecemos los datos en especifico que corresponden a esfuerzo dentro de la base de datos
    dataTeoricoDeformacion = data_teorico['Deformacion[mm]'] #Establecemos los datos especificos que corresponden a deformación
    return dataTeoricoEsfuerzo, dataTeoricoDeformacion #Retornamos los datos especificos anteriormente establecidos


