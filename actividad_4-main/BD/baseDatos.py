from pymongo.mongo_client import MongoClient  #Importamos mongo client de pymongo

#CONEXIÓN
def conexion(): #Definimos conexión 
    uri = "mongodb+srv://jorge:1234@cluster0.cgumkrz.mongodb.net/?retryWrites=true&w=majority" #Establecemos el url con el usuario creado en mongo db 
    # Create a new client and connect to the server
    return MongoClient(uri) #Conectamos el nuevo cliente con la base de datos del servidor de mongo db

#CREATE
""" Código necesario para crear un create en MongoDB"""


#READ
""" Código necesario para crear un read en MongoDB"""
def lecturaDatos(): #Definimos la lectura de datos
    client = conexion() #El cliente esla conexión anteriormente definida
    db = client.actividad4.data_real #Accedemos a la base de datos
    data_list = [] #Definimos los datos de la lista
    for data_real_bd in db.find(): #utilizamos el código para iterar atraves de los documentos almacenados en la colección
        data_list.append(data_real_bd) # Agregamos el siguiente documento obtenido de la iteración 
    return data_list #Volvemos el resultado de la función datalist

#UPDATE
""" Código necesario para actualizar un dato en la BD"""

#DELETE
""" Código necesario para eliminar un dato en la BD"""