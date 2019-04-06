#Crear un archivo llamado 04_if.py
#Crear un script en el que guardéis en una variable un número



numero = int(input("escribe un numero, te dire si es menor a 20 ,  si esta entre 20 i 39 , si esta entre 40 y 59, o si es mayor de 60"))

if numero>60:
    print("el numero: ",numero,"es mas grande que 60")

elif numero<=59 and numero >=40:
    print("el numero: ",numero,"esta entre 40 y 59 ")

elif numero >=20 and numero <=39:
    print("el numero: ", numero, "esta entre 20 y 39")

elif numero <20:
    print("el numero: ", numero, "es mas pequeño que 20")

else :
    print("el numero:",numero," es 60")

#Controlar el tamaño del número en 4 rangos (menor de 20, entre 20 y 39, entre 40 y 59, mayor de 60)
#En cada uno de los casos imprimir por pantalla el número que se haya introducido.
#Subir el archivo a vuestra cuenta de GitHub