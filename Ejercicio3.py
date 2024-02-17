# 3.Realizar un programa que nos pida el ingreso total de un hogar y vaya pidiendo posibles gastos . Como resultado debe decir  todos los egresos y el ahorro.

IngresosTotales=float(input("Ingresa el monto total de ingresos de su familia:"))
Comida=float(input("Ingresa el monto mensual que se gasta en alimentación:"))
Pasajes=float(input("Ingresa el monto mensual que se gasta en pasajes (incluye costos de tarjetas de tren):"))
Servicios=float(input("Ingrese el monto de servicios (agua y luz) que gasta mensualmente:"))
Vestimenta=float(input("Ingrese el monto mensual que gasta en vestimenta:"))
Salidas=float(input("Ingrese el monto mensual que gasta en salidas sociales:"))

EgresosTotales = Comida + Pasajes + Servicios + Vestimenta + Salidas
EgresosFijos = Comida + Pasajes + Servicios
EgresosDiscrecionales = Vestimenta + Salidas
Ahorro = IngresosTotales - EgresosTotales

print("Los gastos totales mensuales son:", EgresosTotales)
print("Los gastos fijos son:", EgresosFijos)
print("Los gastos vanos son:", EgresosDiscrecionales)
print("El ahorro total es:", Ahorro)
