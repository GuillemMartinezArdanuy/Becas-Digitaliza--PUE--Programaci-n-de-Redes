#Crear un archivo llamado 02_list-dict.py
#Crear una lista que contenga varios strings.
listaStrings=["Doraemon","Pingu","Arale","Goku","Athori el ninja","Musculman"]
#Crear una lista que contenga varios integers.
listaIntegers=[10,20,30,40,50,60,70,80,90,100,100,200,300,400,500]
#Crear una lista que contenga strings, integers y floats.
listaMixTypes=["Doraemon","Pingu","Arale","Goku","Athori el ninja","Musculman",10,20,30,40,50,60,70,80,90,100,100,200,300,400,500,50.2,50.3,50.4,50.5,60.2,60.3,60.5]
#Crear las sentencias necesarias para imprimir, por pantalla, la información de las listas.
print("Personatges: ")
for personatge in listaStrings:
    print(personatge)
print("----FI--PERSONATGES----\n")

print("Integers:")
for numero in listaIntegers:
    print(numero)

print("----FI--INTEGEERS----\n")

print("Lista diferentes tipos de Valores: ")
for valor in listaMixTypes:
    print(valor)

print("----FI--LISTA MIX----\n")

#Crear 3 sentencias para asignar, en cada una, el último valor de una lista diferente a una variable (es decir, habrá 3 variables, cada una con el último valor de una de las listas).
listaNuevaAbsorvedora=[]
listaNuevaAbsorvedora.append(listaStrings[-1])
listaNuevaAbsorvedora.append(listaIntegers[-1])
listaNuevaAbsorvedora.append(listaMixTypes[-1])

print(listaNuevaAbsorvedora)
#Crear una sentencia para imprimir, por pantalla, un texto, y concatenar la información de las variables.
print("Uno de los personajes de mi lista  que esta en la posicion 3 es:",listaStrings[2],"\nUn Integer de mi lista en la posicion 2 es: ",listaIntegers[1], "\nEn la lista Mix, en la ultima posicion  penultima tenemos: ",listaMixTypes[-2],"\n")
#Crear un diccionario de vuestras películas/obras favoritas (clave: autor, valor:película)
diccionarioPelisGuillem={"Pamela Lyndon Travers":"Mary Poppins","Quentin Tarantino":"Reservoir Dogs","Guy Ritchie":"Snatch. Cerdos y diamantes"}
#Crear sentencia para imprimir por pantalla todo el diccionario.
print("DICCIONARIO DE AUTORES ----> PELIS:")
print(diccionarioPelisGuillem,"\n")

#Crear sentencia para imprimir por pantalla sólo las claves del diccionario
print("CLAVES DE DICCIONARIO DE AUTORES -->PELIS  ++++ SOLO AUTORES: ")
print(diccionarioPelisGuillem.keys(),"\n")

print("Forma mas correcta: ")
for keys in diccionarioPelisGuillem:
    print(keys)
#Crear sentencia para imprimir por pantalla sólo los valores del diccionario.
print("\nCLAVES DE DICCIONARIO DE AUTORES -->PELIS  ++++ SOLO PELIS: ")
print(diccionarioPelisGuillem.values(),"\n")

print("Forma mas correcta: ")
diccionarioPelisGuillem.values()
for values in diccionarioPelisGuillem:
    print(diccionarioPelisGuillem[values])

#Subir el archivo a vuestra cuenta de GitHub.