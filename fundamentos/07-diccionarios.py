#Diccionarios 

my_dict = dict()
my_other_dict = {}

print(type(my_dict)) # <class 'dict'>
print(type(my_other_dict)) # <class 'dict'>

my_other_dict = {"Nombre": "Jairo", "Apellido": "Rodriguez", "Edad": 19, 1: "Python"}
my_dict = {
    "Nombre": "Jairo", 
    "Apellido": "Rodriguez", 
    "Edad": 19, 
    "Lenguajes": {"Python","Swift","Kotlin"},
    1:1.77
    }
print(my_other_dict)
print(my_dict)

print(len(my_other_dict)) # 4 elementos
print(len(my_dict)) # 5 elementos

print(my_dict["Nombre"]) # Jairo

my_dict["Nombre"] = "Jairo David" # Modifica el valor de la clave "Nombre"
print(my_dict["Nombre"]) # Jairo David

print(my_dict[1]) # 1.77

my_dict["calle"] = "Calle jairor" #se agrega una nueva clave "calle" con su valor al final del diccionario
print(my_dict) # {'Nombre': 'Jairo David', 'Apellido': 'Rodriguez', 'Edad': 19, 'Lenguajes': {'Kotlin', 'Swift', 'Python'}, 1: 1.77, 'calle': 'Calle jairor'}

print("\n----- Imprimir claves del diccionario -----")
for clave in my_dict.keys():
    print(clave) # Imprime las claves del diccionario

print("\n----- Imprimir valores del diccionario -----")
for valor in my_dict.values():
    print(valor) # Imprime los valores del diccionario

print("\n----- Imprimir clave-valor del diccionario -----")
for clave, valor in my_dict.items():
    print(f"{clave}: {valor}") # Imprime las claves y valores del diccionario

print("\n----- Verificar si una clave existe en el diccionario -----")
if "vader" in my_dict:
    print("La clave existe en el diccionario") # La clave 'Nombre' existe en el diccionario
else:
    print("La clave no existe en el diccionario")

print("\n----- Eliminar clave-valor -----")
print(my_dict)
del my_dict["calle"] # Elimina la clave "calle" del diccionario
print(my_dict) # {'Nombre': 'Jairo David', 'Apellido': 'Rodriguez', 'Edad': 19, 'Lenguajes': {'Kotlin', 'Swift', 'Python'}, 1: 1.77}

print("\n----- Comprobar si existe una clave -----")
print("Jairo" in my_dict) # True, verifica si la clave "Jairo" existe en el diccionario
print("Nombre" in my_dict) # True, verifica si la clave "Nombre" existe en el diccionario

print("\n----- Imprimir elementos -----")
print(my_dict.items()) # Imprime todos los elementos del diccionario como pares clave-valor
print(my_dict.keys()) # Imprime todas las claves del diccionario
print(my_dict.values()) # Imprime todos los valores del diccionario

#my_new_dict = my_other_dict.fromkeys({"Nombre", 1, "Piso"}) #crear un diccionario sin valores
my_new_dict = dict.fromkeys({"Nombre", 1, "Piso"}) # crear un diccionario sin valores
print(my_new_dict)

# nombre = input("Ingrese su nombre: ")
# my_new_dict["Nombre"] = nombre # Asigna el valor ingresado por el usuario a la clave "Nombre"
# print(my_new_dict) # Imprime el diccionario con el valor ingresado por el usuario

my_list = ["Nombre",1,"Piso"]
my_new_dict = dict.fromkeys(my_list) # Crear un diccionario a partir de una lista
print(my_new_dict) # Imprime el diccionario creado a partir de la lista

my_new_dict = dict.fromkeys({"Nombre",1,"Piso"})
print(my_new_dict) # Imprime el diccionario creado a partir de un conjunto

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict) # Imprime el diccionario creado a partir de otro diccionario sin valores

#Añade vader como valores para todas las claves del nuevo diccionario
my_new_dict = dict.fromkeys(my_dict,"vader")
print(my_new_dict.values())

print(list(my_new_dict.values())) 
print(tuple(my_new_dict)) #imprime las claves del diccionario como una tupla
print(set(my_new_dict)) #imprime las claves del diccionario como un conjunto