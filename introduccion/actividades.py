def calcular_edad_futura():
    nombre = input("Cuál es tu nombre?")
    edad = int(input("Cuál es tu edad?"))
    edad_futura = edad + 10
    print("Dentro de 10 años", nombre, "tendrá", edad_futura, "años")
    
calcular_edad_futura()


def calcular_area():
    base = float(input("Ingrese la base del rectángulo:"))
    altura= float(input("Ingrese la altura del rectángulo:"))
    area = base * altura
    print("El área del rectángulo es", area)
calcular_area()

