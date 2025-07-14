#Expresiones regulares

import re

#match() busca una coincidencia al inicio de la cadena

my_string = "Esta es la leccion numero 8: Leccion llamada Expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6: Tipos de errores"
match = re.match("Esta es la leccion",my_string,re.I) #verifica si el patron existen en my_string
#SALIDA: <re.Match object; span=(0, 18), match='Esta es la leccion'>

print(match)
start,end = match.span() #Imprime el rango de la coincidencia (posicion) (0,18) es Tupla
print(my_string[start:end]) #despues de desempaquetar se indexa el string para mostrar la coincidencia

match = re.match("Esta no es la leccion",my_other_string)

#if not(match==None) forma de verificar si hay coincidencias
#if match != None otra forma de verificar si hay coincidencia

if match is not None: #entra si hay coincidencia, es distinto de None
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

# print(re.match("Esta es la leccion",my_other_string))
# #Imprime None porque no hay coincidencia

#print(re.match("Expresiones regulares",my_string)) #
#Imprime None porque busca desde el inicio de la cadena

#search
#busca una coincidencia en cualquier parte de la cadena

search = re.search("leccion",my_string,re.I)
print(search) #<re.Match object; span=(11, 18), match='leccion'>
start, end = search.span()
print(my_string[start:end])
# print(type(search.span())) prueba de que span devuelve una tupla

#findall

findall = re.findall("leccion",my_string,re.I) #re.I para Ignore case, ignorar mayusculas y minusculas
print(findall)
print(type(findall)) #lista con todas las ocurrencias de "leccion" en my_string


#split 

print(re.split(":",my_string)) #split busca un separador y devuelve una lista con subcadenas separadas por el separador

