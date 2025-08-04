numero=1
#Bucle while
while numero < 21:
    #Estructuras de control condicional
    if numero % 15 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
    numero += 1 #incrementar el numero
#Fin del bucle while