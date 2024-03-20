import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Vocales
vowels = "aeiou"

# Elegir una palabra al azar
secret_word = random.choice(words)

# Maximo de fallos
max_fails = 5

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")

# Seleccion de dificultad
print("""Ingresa 1 para: Facil
Ingresa 2 para: Media
Ingresa 3 para: Dificil""")

diff = int(input("Selecciona una difficultad: "))

# Verificar que la seleccion es valida
while diff > 3 or diff < 1:
    diff = int(input("Selecciona una dificultad valida: "))
    
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# Modifica la muestra de la palabra secreta dependiendo la dificultad
if diff == 1:
    word_displayed = "".join([letter if letter in vowels else "_" for letter in secret_word])
elif diff == 2:
    word_displayed = secret_word[0] + "_" * (len(secret_word)-2) + secret_word[-1]
else:
    word_displayed = "_" * len(secret_word) 

# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

fails = 0

while fails < max_fails:
    
    # Se cargan las vocales a las letras adivinadas
    if diff == 1:
        for letter in secret_word:
            if letter in vowels:
                guessed_letters.append(letter)
    
    # Se cargan la primer y ultima letra a las adivinadas
    elif diff == 2:
        guessed_letters.append(word_displayed[0])
        guessed_letters.append(word_displayed[-1])
    
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    
    #Verificar si no se ingreso nada
    if letter == "": 
        print("No ingresaste nada..., intentalo otra vez")
        continue
    
    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        fails += 1
    
    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
        break
else:
 print(f"¡Oh no! Has alcanzado los {max_fails} fallos.")
 print(f"La palabra secreta era: {secret_word}")
