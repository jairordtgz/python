#clases

class Person:
    pass

print(Person)
print(Person())

class MyPerson: #definir clase para que reciba parametros
    def __init__(self, name,surname, alias = "sin alias"):
        # self.name = name
        # self.surname = surname
        self.full_name = f"{name} {surname} ({alias})" #propiedad publica
        self.__name = name #propiedada privada a modificacion
        self.__surname = surname

    def get_name(self): #acceder sin modificar
        return self.__name



    def walk(self): #acceder a todo lo guardado en self
        print(f"{self.full_name} Esta caminando")     


my_person = MyPerson("Jairo","Rodriguez") #no hace falta declarar alias
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

# alias definido aunque tenga uno por defecto
my_other_person = MyPerson("Jairo","Rodriguez","jairodri")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Hector de Leon (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 501 #tipado debil 
print(my_other_person.full_name)