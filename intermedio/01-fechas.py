#dates
from datetime import datetime

now = datetime.now() #inicializar variable de tipo datetime

def print_date(date):
    print(date.year) #imprime año
    print(date.month)#imprime mes
    print(date.day) #imprime dia
    print(date.hour)#imprime hora
    print(date.minute)#imprime minutos
    print(date.second)#imprime segundos
    print(date.timestamp())

print_date(now)


year_2025 = datetime(2025,6,22) #lo que no se defina, lo interpreta como 0, se debe pasar año, mes, dia como minimo para que imprima correctamente

print_date(year_2025)

from datetime import time #agrupa horas

current_time = time(21,6,0) #se definen valores, sino imprime 0

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date #solo agrupa fechas, por ende no tiene hour, minute, second

current_date = date.today() #imprimir fecha actual

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2025,6,22) #forma de imprimir fecha pasada como argumentos

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,current_date.month+1,current_date.day)

print(current_date.month)




diff = year_2025 - now
print(diff)
diff = year_2025.date() - current_date
print(diff)

print(year_2025.time)

from datetime import timedelta

start_time_delta = timedelta(200,100,100,weeks=10)
end_time_delta = timedelta(300,100,100,weeks=13)

print(end_time_delta-start_time_delta)
print(end_time_delta+start_time_delta)