lista = [1, "hola", 3.67, [1 , 2 , 3]]
print(lista)
print(lista[-1])
lista_2 =["hola", 2, 3, 4, "aiuda"]
lista_2.append(555) #agrega datos sueltos a la lista
print(lista_2)
lista_2.extend(lista) #añade una lista a otra lista
print(lista_2)
lista_2.insert(2, "casa") #el primer dato define la posicion y el segundo el contenido a agregar a la lista
print(lista_2)
lista_2.remove(555) #remueve el valor escrito dentro del parentesis
print(lista_2)
lista_2.pop(2) #elimina el valor en la posicion ingresada dentro del parentesis y si no  hay nada dentro delparentesis borra el ultimo dato
#las listas se enpieza a contas desde 0
print(lista_2)
lista_2.reverse()#le da vuelta a la lista
print(lista_2)