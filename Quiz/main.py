import requests
import random

def trivia_fetch(num):
    """
    Función obligatoria: recibe un número y devuelve un diccionario
    con trivia de la Numbers API.
    """
    url = f"http://numbersapi.com/{num}/trivia?json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"text": "No se pudo obtener trivia", "number": num, "found": False}
    except Exception as e:
        return {"text": f"Error: {e}", "number": num, "found": False}


def main():
    print("🎉 Bienvenido al Quiz de Números 🎉")
    print("Tendrás 3 rondas. Intenta adivinar el número correcto según la trivia.\n")

    score = 0
    rounds = 3

    for i in range(1, rounds + 1):
        # Generar un número aleatorio entre 1 y 50
        number = random.randint(1, 50)
        trivia = trivia_fetch(number)

        if not trivia["found"]:
            print("Hubo un problema al obtener la trivia. Pasemos a la siguiente pregunta.")
            continue

        print(f"Ronda {i}:")
        print(f"🔹 Pista: {trivia['text']}")

        try:
            guess = int(input("👉 ¿Qué número crees que es? "))
            if guess == trivia["number"]:
                print("✅ ¡Correcto!\n")
                score += 1
            else:
                print(f"❌ Incorrecto. Era el número {trivia['number']}\n")
        except ValueError:
            print("⚠️ Eso no es un número válido. Pasemos a la siguiente ronda.\n")

    print("🎯 Fin del quiz 🎯")
    print(f"Tu puntaje final fue: {score}/{rounds}")

    if score == rounds:
        print("🏆 ¡Perfecto! Eres un genio de los números.")
    elif score > 0:
        print("👏 ¡Bien jugado! Sabes algunas curiosidades.")
    else:
        print("😅 No acertaste, pero aprendiste algo nuevo.")


if __name__ == "__main__":
    main()
