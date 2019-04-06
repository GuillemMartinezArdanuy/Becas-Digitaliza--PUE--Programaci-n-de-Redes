#Crear un archivo llamado 06_for.py
#Crear una lista con nombres de persona e incluir, como mínimo, 5 nombres (como mínimo, uno ha de tener la vocal "a")
listaNombres=["Antonio","Manuel","Jose","Manuela","Antonia","Pepita","Carol","Ivan","Guillem","Alberto","Luis"]
#Crear una lista llamada "selected"
selected=[]
#Recorrer, mediante un for, la lista de los nombres e imprimir un texto con el nombre recorrido en dicha iterración.
#Asimismo, si el nombre de esa iteración contine una "a", añadirlo a la lista llamada "selected"
for nombre in listaNombres:
    print(nombre)
    if 'a' in nombre:
        selected.append(nombre)

print("----FIN DE LA LISTA----\n")




#Finalmente, imprimir por pantalla la lista "selected"
print("imprimimos el valor de la lista SELECTED: ")
print(selected,"\n")
print("imprimimos el valor de la lista SELECTED (mostrando el valor uno por uno, es mas elegante (al menos para mi))")

for nombre in selected:
    print(nombre)

#Subir el archivo a vuestra cuenta de GitHub