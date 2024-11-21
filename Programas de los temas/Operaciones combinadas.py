numero1 = float(input("Introduce el valor de numero1: "))
numero2 = float(input("Introduce el valor de numero2: "))
numero3 = float(input("Introduce el valor de numero3: "))
numero4 = float(input("Introduce el valor de numero4: "))

resultado1 = numero1 + numero2 * numero3
print("Resultado de numero1 + numero2 * numero3:", resultado1)

resultado2 = (numero1 + numero2) * numero3
print("Resultado de (numero1 + numero2) * numero3:", resultado2)

resultado3 = numero1 * numero2 ** numero3
print("Resultado de numero1 * numero2 ** numero3:", resultado3)

resultado4 = numero1 / numero2 + numero3
print("Resultado de numero1 / numero2 + numero3:", resultado4)

resultado5 = (numero1 + numero2) * numero3 - numero4 ** numero3 / numero2
print("Resultado de (numero1 + numero2) * numero3 - numero4 ** numero3 / numero2:", resultado5)

resultado6 = (numero1 + numero2) % numero3 + numero4 // numero2
print("Resultado de (numero1 + numero2) % numero3 + numero4 // numero2:", resultado6)
