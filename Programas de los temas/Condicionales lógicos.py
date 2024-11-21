numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

resultado_and = (numero1 > 5 and numero2 < 10)
print(f"Ambos números son válidos: numero1 > 5 y numero2 < 10 -> {resultado_and}")

resultado_or = (numero1 > 5 or numero2 < 10)
print(f"Al menos una condición es verdadera: numero1 > 5 o numero2 < 10 -> {resultado_or}")

resultado_not = not (numero1 == numero2)
print(f"Los números no son iguales -> {resultado_not}")

resultado_combinado = (numero1 > 0 and numero2 < 0) or numero1 == numero2
print(f"Número 1 es positivo y Número 2 es negativo, o los números son iguales -> {resultado_combinado}")