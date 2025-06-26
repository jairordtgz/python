# list comprenhension

my_original_list = [0,1,2,3,4,5,6,7]
print(my_original_list)

my_list = [i + 1 for i in range(8)] #si queremos hasta el 7, se pone 8 pq no incluye

print(my_list)

my_range = range(8)

print(list(my_range))

my_list = [i * 2 for i in range(8)]
print(my_list)

my_list = [i*i for i in range(8)]
print(my_list)

def sumfive(num):
    return num + 5

my_list = [sumfive(i) for i in range(8)]
print(my_list)

#fibonacci primeros n numeros

def fibonacci(num):
    lista = []
    i = 2
    pos = 1
    lista.append(0)
    lista.append(1)
    while(i<num):
        lista.append(lista[pos]+lista[pos-1])
        pos = pos + 1
        i = i + 1

    print(lista)
        
fibonacci(10)