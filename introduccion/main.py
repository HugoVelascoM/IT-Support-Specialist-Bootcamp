print("¡Hola, mundo!")
nombre = "Hugo"
edad = 22
estudia = True 
altura = 1.70
print("Mi nombre es", nombre, "Mi edad es", edad, "Estudia", estudia, "Mi altura es" , altura)
print(type(nombre))

#función básica

def saludar():
    print("Hola, mundo desde una función")
saludar()

def presentar(nombre, edad):
    print("Hola mi nombre es", nombre, "y tengo", edad, "años")
presentar("Hugo", 22)

def sumar(a, b):
    resultado= a + b
    print("la suma de", a, "y", b, "es", resultado)
sumar(13422, 5001)
