#modulos 
#usar codigo de otros ficheros
import my_module 
#from 10-funciones import sum_two_values no es valido como fichero a importar como modulo
my_module.sumValues(5,3,2)
my_module.printValue("hola python")

from my_module import sumValues, printValue #importar solo las funciones especificadas
sumValues(5,6,1)
printValue("hola python")

import math
print(math.pi)
print(math.pow(2,8))

from math import pi as PI_VALUE #importar propiedad concreta y renombrarla
print(PI_VALUE)