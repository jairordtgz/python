#Funciones 
def my_function():
    print("Esto es una funcion")


my_function()
my_function()
my_function() 

def sum_two_values(a,b):
    return a+b
    #tambien se puede con print(a+b)

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero: "))
print(sum_two_values(n1,n2))
# sum_two_values(n1,n2) #no imprime 
print(sum_two_values("5","7")) #concatena cadenas de texto, no suma
print(sum_two_values(1.4,5.2))


def print_name(name,surname):
    print(f"{name} {surname}")

print_name("Jairo","Rodriguez")

print_name(surname="Rodriguez",name="Jairo")

def print_name_with_default(name,surname,alias = "sin alas"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Jairo","Rodriguez","jairorti")

def print_texts(*texts):
    for text in texts:
        print(text.upper())

print_texts("Hola")
print_texts("Jairo","Rodriguez","jairordtgz")