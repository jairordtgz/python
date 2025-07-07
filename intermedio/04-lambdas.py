#lambdas 
#funciones sin nombre

sum_two_values = lambda a,b: a + b

print(sum_two_values(2,4))

multiply_values = lambda a,b: a*b - 3
print(multiply_values(2,4))

def sum_three_values(value):
    return lambda a,b: a + b + value

print(sum_three_values(5)(2,4))