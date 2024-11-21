numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

condicion1 = numero1 > 5 and numero2 < 10
condicion2 = numero1 == numero2
condicion3 = numero1 != numero2
condicion4 = numero1 > 0 or numero2 < 0
condicion5 = not (numero1 == numero2)

print(f"¿numero1 > 5 y numero2 < 10? -> {condicion1}")
print(f"¿numero1 es igual a numero2? -> {condicion2}")
print(f"¿numero1 es diferente de numero2? -> {condicion3}")
print(f"¿numero1 es mayor que 0 o numero2 es menor que 0? -> {condicion4}")
print(f"¿numero1 no es igual a numero2? -> {condicion5}")
