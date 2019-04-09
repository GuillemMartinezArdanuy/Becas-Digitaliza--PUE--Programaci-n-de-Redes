
lista=[1,1,2]

def Unos_A_Los_Extremos(lista):
    lista=[1,lista[-1]+1,1]
    return lista

def Uno_Al_Medio(lista):
    lista=[lista[1]+1,1,lista[1]+2]
    return lista

iteraciones=int(input("number of iterations?"))
for i in range (iteraciones):
    lista=Unos_A_Los_Extremos(lista)
    print(lista)
    lista=Uno_Al_Medio(lista)
    print(lista)
