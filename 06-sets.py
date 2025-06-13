#sets 

my_set = set()
my_other_set = {}
print(type(my_set)) # <class 'set'>
print(type(my_other_set)) # <class 'dict'>

my_other_set = {"Jairo","David",19}
print(type(my_other_set)) # <class 'set'>

print(len(my_other_set)) # 3 elementos
# print(my_other_set[0]) # TypeError: 'set' object is not subscriptable
my_other_set.add("jairodri")
print(my_other_set) # {'jairodri','Jairo', 19, 'David'}
#imprime en cualquier orden por que no es estructura de tipo ordenada
my_other_set.add("jairodri")#un set no acepta repeditos
print(my_other_set)
#hacer busquedas 
print("Jairo" in my_other_set) # True
my_other_set.remove("Jairo")
print(my_other_set) # {'jairodri', 19, 'David'}

my_other_set.clear() #elimina todos los elementos
print(my_other_set) # set()
print(len(my_other_set)) # 0
#las ventajas son para los que prefierem usar estrcturas no ordenadas

del my_other_set
#print(my_other_set) # NameError: name 'my_other_set' is not defined

my_set = {"Jairo", "David", 19}

lista = list(my_set)
print(lista) # ['David', 19, 'Jairo']
print(lista[0]) #puede salir cualquir elemento por que no es ordenada

my_other_set = {"kotlin","swift","python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_new_set).union("javascript","C#")) # muestra el set sin repeticiones y con los nuevos elementos declarados en union

print(my_new_set.difference(my_set)) # {'kotlin', 'swift', 'python'} en diferente orden