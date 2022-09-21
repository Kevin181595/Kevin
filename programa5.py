"""
EJERCICIO 1
Realizar un programa que simule tirar
dos dados y luego muestre los
valores que aparecieron. Si la suma
de dichos números es igual a 9
mostrar un mensaje de “Has ganado”
sino mostrar “Has perdido”.
"""

import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
suma = dado1 + dado2

if suma == 9:
    print("Ganaste....!!!")
else:
    print("perdiste...!!!")
    
