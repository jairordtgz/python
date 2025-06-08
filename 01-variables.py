print("Hola mundo")
#Se usa minusculas o snake_case para las variables
variable = "primer texto"
print(variable)

my_int_variable = 10
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

print(variable,my_int_variable,my_bool_variable)
# type() nos dice el tipo de dato de la variable
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Funcion len() nos dice la longitud de una cadena

print(len(my_int_to_str_variable))
print(len(variable)) #primer texto contiene 12 caracteres

print("Este es el valor de:",my_bool_variable)


nombre, apellido, alias, edad = "jairo", "rodriguez", "jairodri", 19

print("Me llamo",nombre,apellido,". Mi edad es",edad,"y mi alias es",alias)


#Inputs
#esto ejecuta en terminal, no en salida
#se puede usar la misma variable para guardar el input porque se sobreescribe

"""
primer_nombre = input('Cual es tu primer nombre:')
edad = input('Cual es tu edad:')
print(primer_nombre)
print(edad)
"""

#tratar de forzar el tipo de dato
adress: str = "direccion"
adress = 32
adress = True
adress = 3.14
print(type(adress))


