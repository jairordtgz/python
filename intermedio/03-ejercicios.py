# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
#  Múltiplos de 3 por la palabra "fizz".
#  Múltiplos de 5 por la palabra "buzz".
#  Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
# 
print("----- Ejercicio 1: -----")
for i in range(1,101):
    if(i%3==0 and i%5==0):
        print("fizzbuzz")
    elif (i%3==0):
        print("fizz")
    elif(i%5==0):
        print("buzz")
    else:
        print(i)


# 
print("----- Ejercicio 2: -----")

#  Escribe una función que reciba dos palabras (String) y retorne
#  verdadero o falso (Bool) según sean o no anagramas.
#  Un Anagrama consiste en formar una palabra reordenando TODAS
#  las letras de otra palabra inicial.
#  NO hace falta comprobar que ambas palabras existan.
#  Dos palabras exactamente iguales no son anagrama.

#def esAnagrama(palabra1,palabra2):
    
    #if (palabra1 == palabra2)

# palabra = "Jairo"
# lista = []
# for letra in palabra:
#     lista.append(letra.lower())
#     if('a' in lista):
#         print("la a esta en la lista")

# print(lista)

def esAnagrama(palabra1,palabra2):
    if (palabra1 == palabra2):
        return False

    listap1 = []
    listap2 = []

    for l1 in palabra1:
        listap1.append(l1.lower())
    
    for l2 in palabra2:
        listap2.append(l2.lower())

    if(listap1.sort() == listap2.sort()):
        return True
    else:
        return False

print(esAnagrama("vader","radev"))

#  Escribe un programa que imprima los 50 primeros números de la sucesión
#  de Fibonacci empezando en 0.
#  La serie Fibonacci se compone por una sucesión de números en
#  la que el siguiente siempre es la suma de los dos anteriores.
#  0, 1, 1, 2, 3, 5, 8, 13

print("----- Ejercicio 3 -----")
lista = []
lista.append(0)
lista.append(1)
i = 3
pos = 1
while (i<=50):
    lista.append(lista[pos]+lista[pos-1])
    i = i + 1
    pos = pos + 1

for numero in lista:
    print(numero)

print("------ Ejercicio 4 ------")

# Crea un programa se encargue de transformar un número
# decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

def decimal_a_binario(num):
    residuos = []
    while(num>0):
        residuo = num%2
        residuos.append(residuo)
        num = num // 2

    residuos.reverse()
    binario = ''.join(str(bit) for bit in residuos)
    print(binario)

decimal_a_binario(5)

print("---- Ejercicio 5 ----- ")

def factorialRecursivo(num):
    if(num==0):
        return 1
    
    return num*factorialRecursivo(num-1)

print(factorialRecursivo(3))

numero = 253

