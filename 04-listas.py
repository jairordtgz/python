#Listas

lista = list()
otra_lista = []
print(len(lista)) #longitud de la lista

lista = [35,24,62,52,30,30,17]

print(lista)
print(len(lista)) 
#lista cualquier tipo de dato
otra_lista = [35,1.77,"Jairo","Rodriguez"]

print(type(otra_lista))
print(otra_lista)

print(otra_lista[0]) #0 primer elemento
print(otra_lista[1]) #1 segundo elemento
print(otra_lista[-1]) #-1 imprime el ultimo elemento
print(otra_lista[-3]) #-3 imprime el tercer elemento desde el final
print(otra_lista[-4]) #-4 imprime el cuarto elemento desde el final
#print(otra_lista[-5]) IndexError: list index out of range

print(otra_lista.count("Jairo"))
 #cuenta cuantas veces aparece un elemento en la lista otra_lista

print(lista.count(30)) #hay dos veces el 30 en la lista lista

#Desempaquetado de listas
print("----Desempaquetado de listas----")
edad, altura, nombre, apellido = otra_lista #asignacion por orden y variables acordes 

print(edad)      #35
nombre, altura, edad,apellido = otra_lista[2], otra_lista[1], otra_lista[0], otra_lista[3] #asignacion manual
print(edad)


print("Imprimir con bucle")
for i in range(len(otra_lista)):
    print(otra_lista[i])
    
print(lista+otra_lista) #primero lista luego otra_lista

# lista = "Hola Python"
# print(lista)  #imprime la cadena de texto
# print(type(lista))  #imprime el tipo de dato, en este caso str
# lista = list(lista)  #convierte la cadena de texto en una lista de caracteres
# print(lista)  #imprime la lista de caracteres
# print(type(lista))  #imprime el tipo de dato, en este caso list 

otra_lista.append("jairodri")
print(otra_lista)  #añade el elemento al final de la lista

otra_lista.insert(1,"rojo") #añade el elemento en la posicion 1 de la lista
print(otra_lista)  #añade el elemento en la posicion 1 de la lista

otra_lista[1] = "azul"
print(otra_lista)  #modifica el elemento en la posicion 1 de la lista
otra_lista.remove("azul")  #elimina el elemento de la lista
print(otra_lista)  #imprime la lista sin el elemento eliminado

lista.remove(30)
print(lista)  #imprime la lista sin el elemento eliminado

#lista.pop()  #elimina el ultimo elemento de la lista
print(lista.pop()) #imprime y elimina el ultimo elemento de la lista
print(lista)  #elimina el ultimo elemento de la lista

print(lista.pop(2))
print(lista)  #elimina el elemento en la posicion 2 de la lista

# lista = [1,2,3,4,5,6,7,8,9,10]
# nuevalista = []
# print(len(lista))

# print("---Invertir una lista---")
# print("Lista original:", lista)

# for i in range(len(lista)):
#     numero = lista.pop()
#     nuevalista.append(numero)

# print("Nueva lista:", nuevalista)
print(lista)
del lista[2]  #elimina el elemento en la posicion 2 de la lista, es decir 52
print(lista)  #elimina el elemento en la posicion 2 de la lista


copia_lista = lista.copy()

#del elimina por indice, remove elimina por valor

lista.clear()  #elimina todos los elementos de la lista
print(lista)  #imprime la lista vacia
print(copia_lista)  #imprime la copia de la lista original

#invertir lista
copia_lista.reverse()
print(copia_lista)  #invierte la lista, no devuelve nada, solo la invierte

copia_lista.sort()
print(copia_lista)  #ordena la lista de menor a mayor


# copia_lista.sort(reverse=True)
# print(copia_lista)  #ordena la lista de mayor a menor

print(copia_lista[1:2])
print(copia_lista[1:3])