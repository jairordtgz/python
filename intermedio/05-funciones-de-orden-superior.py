#Funciones de orden superior

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(a,b,f): # f es variable que contiene la funcion
    return f(a+b)

print(sum_two_values_and_add_value(5,2,sum_one))
print(sum_two_values_and_add_value(5,2,sum_five))


#Closures
def sum_ten(original_value): #funcion que retorna una funcion
    def add(value):
        return value+10+original_value
    return add
    

add_closure = sum_ten(1)

print(add_closure(5))

print((sum_ten(5))(1))

#Built-in high order functions

#Map

def multiply_two(number):
    return number*2

numbers = [2,5,10,21,3,30]
print(list(map(multiply_two,numbers))) #con funcion
print(list(map(lambda number:number*2,numbers))) #con lambda

#Filter 
def filter_mayores_que_10(number):
    return number > 10

print(list(filter(filter_mayores_que_10,numbers))) #con funcion
print(list(filter(lambda number: number>10,numbers))) #con lambda

#Reduce 
from functools import reduce

def sum_two_values(a,b):
    print(a)
    print(b)
    return a + b

print(reduce(sum_two_values,numbers))