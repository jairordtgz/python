#Tipos de error

#Sintax error 

#print "Hola mundo" #error de sintaxis
print("Hola mundo")

#Name error 
variable = "Jairo" #si comento esto: variable no esta definido
print(variable) #variable no definida

#Index error
lista = ["python","swift","Kotlin","Dart","javascript"]

print(lista[0])
print(lista[-1])
#print(lista[5]) #error de indice, indice fuera de rango

#ModuleNotFoundError

#import maths  #no hay modulo maths 
import math      


#AttributeError
#print(math.PI) #modulo math no tiene atributo PI
print(math.pi)

#KeyError

dic = {"Nombre": "Jairo","Apellido": "Rodriguez","Edad":19,1: "Python"}

print(dic["Edad"]) #Imprime 19
#print(dic["Apelido"]) #KeyError: clave Apelido no existe
print(dic["Apellido"])


#TypeError
#print(lista["Apellido"]) #no puede indexar con str
#print(lista["0"]) #otro type error, "0" no es entero
print(lista[0])


#ImportError

# from math import PI #no se puede importar PI desde math
from math import pi
print(pi)

#ValueError

#my_int = int("10")


# my_int = int("10 años")
# print(type(my_int)) #no se puede convertir "10 años" en entero

#ZeroDivisionError

print(10/0)



