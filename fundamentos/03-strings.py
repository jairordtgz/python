#strings

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))  # longitud de la cadena
print(len(my_other_string))

print(my_string+ " " +my_other_string)  # concatenación de cadenas

my_new_line_string = "Mi string\ncon salto de linea"
print(my_new_line_string)  # salto de línea

my_tab_string = "\t Mi string con tabulacion"
print(my_tab_string)  # tabulación

my_scaped_string = "\\tEste es un string \\n escapado"
print(my_scaped_string)  # string escapado

#formateo 

#String %s
#entero %d
name, surname, edad = "Jairo", "Rodriguez", 19
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,edad))

print("Mi nombre es %s %s y mi edad es %d"% (name, surname, edad))

#evitar esta manera de concatenar cadenas
#print("Mi nombre es " + name + " " + surname + " y mi edad es " + edad) # Esto no funciona porque edad es un entero, no una cadena
#funcionaria si se convierte a cadena con str(edad)

#concatenar por inferencia
print(f"Mi nombre es {name} {surname} y mi edad es {edad}")


#Desempqquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(e) 
print("Hola")


#division

language_slice = language[1:3] # slicing, obtiene los caracteres desde el índice 1 hasta el 2 (el 3 no se incluye)  
print(language_slice) 

language_slice = language[1:] # slicing, obtiene los caracteres desde el índice 1 hasta el final  
print(language_slice) 

language_slice = language[-2]  # slicing, obtiene el penúltimo carácter
print(language_slice) 

language_slice = language[0:6:2]  # slicing, obtiene los caracteres desde el índice 0 hasta el 5 (el 6 no se incluye) con un paso de 2
print(language_slice) 

#dar la vuelta a una cadena
reversed_language = language[::-1]  # slicing, obtiene la cadena al revés
print(reversed_language)

#Funciones

print(language.capitalize()) #agrega la primera letra en mayúscula
print(language.upper())  # convierte toda la cadena a mayúsculas
print(language.count("t"))  # cuenta cuántas veces aparece "t" en la cadena
print(language.isnumeric())  # verifica si la cadena es numérica (retorna False porque "python" no es numérico)
print("1".isnumeric())  # verifica si "1" es numérico (retorna True)
print(language.lower())  # convierte toda la cadena a minúsculas
print(language.upper().isupper())  # verifica si la cadena está en mayúsculas (retorna True)
print(language.lower().isupper())  # verifica si la cadena está en minúsculas (retorna False)
print(language.startswith("py"))  # verifica si la cadena comienza con "py" (retorna True)
print(language.startswith("Py")) # verifica si la cadena comienza con "Py" (retorna False)
print("Py" == "py") # compara "Py" con "py" (retorna False)
