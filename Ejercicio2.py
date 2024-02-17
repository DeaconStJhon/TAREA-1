# 2.Realizar un programa que calcule el area y el perimetro de un poligono a tu eleccion( triangulo , cuadrado , circulo)
## Calcularemos el area  y perimetro del triangulo

import math

Base= float(input("ingresa la base del triangulo:"))
Altura= float(input("ingresa la altura del triangulo:"))
Lado1=float(input("Ingresa el primer lado del triangulo:"))
Lado2=float(input("Ingresa el segundo lado del triangulo:"))
Lado3=float(input("Ingresa el tercer lado del triangulo:"))
Area= (Base*Altura)/2
Perimetro= Lado1+Lado2+Lado3
print("Area del triangulo:",Area)
print("Perimetro del triangulo:",Perimetro) 