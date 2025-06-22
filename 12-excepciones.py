#excepciones
n1, n2 = 5,1
n2 = "1"

#try except
try: 
    print(n1+n2)
    print("No se ha producido error")
except:
    print("Se ha producido un error")


#try except else finally

#else y finally son opcionales

try: 
    print(n1+n2)
    print("No se ha producido error")
except:
    print("Se ha producido un error")
else: #se ejecuta cuando el bloque try no genera error
    print("La ejecucion continua correctamente")
finally: #ejecuta siempre
    print("la ejecucion continua")

try:
    print(n1+n2)
    print("no se ha producido error")
except TypeError: #se ejecuta solo si ocurre TypeError
    print("se ha producido un typeerror")
except ValueError: #se ejecuta solo si ocurre ValueError
    print("se ha producido un valueerror")


#capturar la informacion de la excepcion

try:
    print(n1+n2)
    print("no se ha producido error")
except TypeError as te: #se ejecuta solo si ocurre TypeError
    print(te)
except Exception as error: #excepcion generica
    print(error)
    