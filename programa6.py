"""
EJERCICIO 2
Desarrollar un programa que calcule el
área de las siguientes figuras: cuadrado,
rectángulo, trapecio. Dividir el programa
en 4 partes, 3 módulos, cada módulo
tendrá una función que calcule el área de
un cuadrado, de un rectángulo, de un
trapecio y por otro lado un archivo que
permita la ejecución de dichas funciones.

"""

from area_cuadrado import cuadrado
from area_rectangulo import rectangulo
from area_trapecio import trapecio

lado = int(input("ingrese el lado del cuadrado: "))
print("el area es: ", cuadrado(lado))

base = int(input("ingrese la base del rectangulo: "))
altura = int(input("ingrese la altura del rectangulo:  "))
print("el area es: ", rectangulo(base, altura))

bmayor =  int(input("ingresa la base mayor del trapecio:  "))
bmenor = int(input("ingresa la base menor del trapecio:  "))
altura = int(input("ingrese la altura del trapecio:  "))
print("El area del trapecio es: ", trapecio(bmayor,bmenor,altura) )
