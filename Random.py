import random  # Importa el módulo random

numero_intentos = 0
numero_min = 0
numero_max = 100
cualquiera = random.randint(0, 100)
print("Adivina el número en el que estoy pensando del " + str(numero_min) + " al " + str(numero_max))

while numero_intentos < 10:
    print("Ingresa un número. Tienes 10 oportunidades para adivinar:")
    numeros = input()
    numeros = int(numeros)

    if numeros < cualquiera:
        print("Tu número es mayor .")
    elif numeros > cualquiera:
        print("Tu número es menor.")
    else:
        print("¡Acertaste el número, FELICITACIONES! El número era " + str(cualquiera))
        break

    numero_intentos += 1

if numero_intentos >= 10:
    print("Fin del juego. Agotaste tus 10 intentos. El número era " + str(cualquiera))