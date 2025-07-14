#Archivos 

#archivos txt
import os
f = open("intermedio/my_file.txt","r+") #r+ para leer y escribir, w+ para escribir
#f.write("Mi nombre es Jairo\n Mi apellido es Rodriguez\n tengo 19 \n Estoy repasando Python")
#print(f.read())
print(f.read(10)) #lee primeros 10 caracteres
print(f.readline()) #lee primera linea 
print(f.readline()) #lee segunda linea
#print(f.readlines()) #arreglo con todas las lineas 

for line in f.readlines():
    print(line)

f.write("\nAunque tambien me gusta java") #escribir en siguiente linea
print(f.readline())

f.close()

with open("intermedio/my_file.txt","a") as my_other_file: #a para agregar contenido al final del archivo
     my_other_file.write("\nY swift")
     


#os.remove("intermedio/my_file.txt")


#.json file
import json 
json_file = open("intermedio/my_file.json","w+") #crear un archivo .json
json_test = {
    "name":"Jairo",
    "surname":"Rodriguez",
    "age":19,
    "language":["python","swift","kotlin"],
    "website":"https://moure.dev"} #contenido del archivo json 

json.dump(json_test,json_file,indent=2) #indent para que se vea linea debajo de otra y con indentacion

#json.dump(json_test,json_file,indent=2) #escribe a continuacion

json_file.close()

# for line in json_file.readlines():
#     print(line)

with open("intermedio/my_file.json") as my_other_file: #leer json
     for line in my_other_file.readlines():
          print(line) 


json_dict = json.load(open("intermedio/my_file.json")) #transformar json a diccionario
print(json_dict)
print(type(json_dict)) #diccionario 
print(json_dict["name"])

# .csv file
import csv

csv_file = open("intermedio/my_file.csv","w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name","surname","age","language","website"])
csv_writer.writerow(["Jairo","Rodriguez",19,"python","https://moure.dev"]) 
csv_writer.writerow(["Roswell","",2,"COBOL",""])


csv_file.close()

with open("intermedio/my_file.csv") as my_other_file:
     for line in my_other_file.readlines():
          print(line)



# .xlsx file
#import xlrd #se debe instalar el modulo

# .xml file
import xml
