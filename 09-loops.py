# Loops 
#while 

my_condition = 0
while my_condition < 10:
    print(f"Mandamiento {my_condition} ")
    my_condition += 2
if my_condition == 10:
    print("Mi condicion es igual que 10")
else:
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("se detiene la ejecucion")
        break

    print(my_condition)

print("La ejecucion continua")

#For: iterar listado de elementos
print("------- For -------")
my_list = [35,24,62,52,30,30,17]

for element in my_list:
    print(element)

my_tuple = (35,1.77,"Brais","Moure","Brais")

for element in my_tuple:
    print(element)


my_set = {"Brais","Moure",35}

for element in my_set:
    print(element)


my_dict = {"Nombre": "Jairo", "Apellido": "Rodriguez", "Edad": 19, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")

print("La ejecucion continua")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")