numero_correcto = 5
respuesta = int(input("Adivina el número que estoy pensando (entre 1 y 10): "))
mensajes = ["Lo siento, ese no es el número. ¡Intenta de nuevo!", "¡Felicidades! Adivinaste el número."]

print(mensajes[respuesta == numero_correcto])
