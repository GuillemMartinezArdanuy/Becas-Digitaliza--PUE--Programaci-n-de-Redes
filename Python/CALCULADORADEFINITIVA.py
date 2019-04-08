opcionUsuario = 1  # el numero que quiere el usuario que correspondera a la operacion que nosotros le ofrecemos si es 0 significa que el usuario quiere salir como le indicamos

while opcionUsuario!=0:
    primero = 0  # en suma sera sumando 1 ,en resta sera minuendo , en multiplicacion sera factor 1, en exponencial sera la base
    segundo = 0  # en suma sera sumando 2 , en resta sera sustraendo, en multiplicacion sera factor 2,en  exponencial sera exponente
    resultado = 0.0

#definimos variables booleanas, a modo de control
    entradaOperacionOK = False  # controlaremos que el numero seleccionado del usuario sea un valor que corresponda a una operacion que hemos programado.
    entradaPrimeroOK = False # controlamos que el primer valor sea correcto
    entradaSegundoOK=False # controlamos que el segundo valor sea correcto

    def Suma(primero, segundo):
        try:
            resultado = primero + segundo
            return resultado
        except:
            return None


    def Resta(primero, segundo):
        try:
            resultado = primero - segundo
            return resultado
        except:
            return None


    def Multiplicacion(primero, segundo):
        try:
            resultado = primero * segundo
            return resultado
        except:
            return None

    def Division(primero,segundo):
        try:
            resultado=primero / segundo
            return resultado
        except:
            return None

    def Exponencial(primero, segundo):
        try:
            resultado = primero ** segundo
            return resultado
        except:
            return None

    while entradaOperacionOK == False:  # iniciamos a falso, cuando la operacion sea un valor de una de nuestras claves de opciones de operacion, cambiara a true, i seguira el programa
        print("------------------------------- MENU CALCULADORA -------------------------------")
        print("ingresa un numero correspondiente a la operacion, que deseas realizar: ", "1 -> suma", "2 -> resta",
              "3 -> multiplicacion", "4 -> division", "5 -> exponencial", "0 -> salir", sep="\n")

        try: # seleccionamos la operacion a realizar, usando el  valor introducido por el usuario (integer)
            opcionUsuario = int(input("tu opcion: "))

            if opcionUsuario==0:
                entradaOperacionOK = True # ponemos los controles atrue, para asi llegar al final i poder salir sin problemas
                entradaPrimeroOK =True
                entradaSegundoOK=True
                break

            elif opcionUsuario > 0 and opcionUsuario < 6:
                entradaOperacionOK = True

            else:
                print("tienes que introducir 0,1,2,3,4 o 5")
        except:
            print("-----¡¡¡¡ERROR!!!!----\nintroduce un numero 0,1,2,3,4 o 5")

    while entradaPrimeroOK == False:
        try:
            primero = float(input("introduce el primer valor"))
            entradaPrimeroOK = True # sino ha surgido ningun error, marcamos como la entrada correcta
        except:
            print("error debes introducir un float o un integer") # sale error, i permite volver al try, porque esta dentro del while controlado por entradaPrimeroOk
            entradaPrimeroOK = False # marcamos la entrada como erronea, asi nos obligamos a pedir al usuario el valor que el quiera

    while entradaSegundoOK == False:
        try:
            segundo = float(input("introduce el segundo valor"))
            if opcionUsuario==4 and segundo== 0:
                print("no se dividir entre 0, canvia el valor por favor")
                entradaSegundoOK=False
            else:
                entradaSegundoOK = True
        except:
            print("error debes introducir un float o un integer")
            entradaSegundoOK = False # lo mismo que en la primera


    diccionarioTotal = {1: {"Suma": [primero, segundo, Suma(primero, segundo)]},
                        2: {"Resta": [primero, segundo, Resta(primero, segundo)]},
                        3: {"Multiplicacion": [primero, segundo, Multiplicacion(primero, segundo)]},
                        4: {"Division": [primero, segundo, Division(primero, segundo)]},
                        5: {"Exponencial": [primero, segundo, Exponencial(primero, segundo)]}}

    nombreSeleccionadoOperacion = ""
    try:
        for keys in diccionarioTotal[opcionUsuario]: # recorremos el diccionario con el  valor de las claves que ha introducido el usuario anteriormente
            nombreSeleccionadoOperacion = keys # guardamos este valor en una variable, para no tener que escribir tanto codigo
    except:
        pass

    try:
        resultadoMostrar = (diccionarioTotal[opcionUsuario][nombreSeleccionadoOperacion][2]) # entramos al valor de la funcion que corresponde a lo seleccionado por el usuario
        print("La {0} de {1} y {2} es =  {3}".format(nombreSeleccionadoOperacion, primero, segundo, resultadoMostrar)) # formateamos elegantemente un output, para mostrar el resultado
        entradaOperacionOK = False # una vez mostrado el resultado, marcamos entrada operacionOK, de esta forma volvemos al menu sin problemas
    except:
        pass

else:
    print("¡¡¡ BYE BYE BYE !!!")
