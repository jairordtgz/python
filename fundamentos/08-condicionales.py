#Condicionales

# edad = int(input("Ingrese su edad: "))
# if(edad >= 18):
#     print("Eres mayor de edad")
# else:
#     print("Eres menor de edad")

my_condition = 5*3
if my_condition == 10: #lo mismo que if my_condition == True
    print("Se ejecuta la condicion del if") #se ejecuta solo si my_condition es True



my_condition = 5*5

if my_condition == 10:
    print("Se ejecuta la condicion del segundo if") #se ejecuta si my_condition es diferente de 0, None, False, "", [], {}, etc.

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual a 10 o mayor o igual a 20")

print("La ejecucion continua")

my_string = ""

if not my_string:
    print("La cadena de texto es vacia")

if my_string == "Mi cadena de textooo":
    print("Las cadenas de texto coinciden")