#tuplas 
tupla = tuple()
otra_tupla = ()

tupla = (35,1.77,"Jairo","Rodriguez","Jairo")
otra_tupla = (35,60,30)

print(tupla)
print(type(tupla))

print(tupla[0])
print(tupla[-1])
# print(tupla[4]) #IndexError: tuple index out of range
# print(tupla[-6]) IndexError: tuple index out of range

print(tupla.count("Jairo")) # cuenta cuantas veces aparece un elemento
print(tupla.index("Rodriguez")) # devuelve el indice del elemento
print(tupla.index("Jairo"))   
# tupla[1] = 1.80 #no se puede modificar un elemento de una tupla, es inmutable
# print(tupla)
#print(tupla+otra_tupla) # se pueden concatenar tuplas
my_sum_tuple = tupla + otra_tupla
print(my_sum_tuple)
print("-----Slicing en tuplas-----")
print(my_sum_tuple[3:6])  #slice de tuplas
print(my_sum_tuple[3:])  #slice de tuplas desde el indice 3 hasta el final
print(my_sum_tuple[:3])  #slice de tuplas desde el inicio hasta el indice 3
print(my_sum_tuple[-3:])  #slice de tuplas desde el indice -3 hasta el final

tupla = list(tupla)
print(type(tupla))

tupla[4] = "jairodri" #agrega jairodri en la posicion 4
tupla.insert(1,"azul")
tupla = tuple(tupla) #convierte la lista de nuevo a tupla
print(tupla)
print(type(tupla))

del tupla[2] #tupla no se puede eliminar un elemento, es inmutable
del tupla #elimina la tupla
# print(tupla) #NameError: name 'tupla' is not defined
