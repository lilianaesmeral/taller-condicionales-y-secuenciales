#Liliana Esmeral
#Primer ejercicio
dinero1 = float(input("¿Cuánto dinero invirtió la primera persona?\n"))
dinero2 = float(input("¿Cuánto dinero invirtió la segunda persona?\n"))
dinero3 = float(input("¿Cuánto dinero invirtió la tercera persona?\n"))
total = dinero1+dinero2+dinero3
p1 = (dinero1/total)*100
p2 = (dinero2/total)*100
p3 = (dinero3/total)*100
print(f'''La primera persona invirtió el {p1}%,
la segunda el {p2}% y la tercera el {p3}%''')

#Segundo ejercicio
base = float(input("Digite el sueldo base del empleado\n"))
hijos = int(input("Digite la cantidad de hijos que tiene el empleado\n"))
bonificacion = hijos * 80000
total = base + bonificacion
print(f"La cantidad de bonificación es: {bonificacion}, por lo que el monto total es: {total}")

#Tercer ejercicio
monto = float(input("Digite el monto ahorrado por la persona\n"))
tiempo = int(input("Digite el número de meses para calcular el interés\n"))
saldo_final = (tiempo*monto*0.015)+monto
print(f"Según los datos introducidos, el saldo final luego de {tiempo} meses será {saldo_final}")

#Cuarto ejercicio
metros = float(input("Digite la cantidad de metros cuadrados del terreno a comprar\n"))
total = 80000 * metros
cuota1 = total * 0.35
cuotas = (total-cuota1)/12
print(f'''El monto total por la compra del terreno es: {total}, 
la cuota inicial es {cuota1} 
y el resto de cuotas (en 12 meses) {cuotas}''')

#Quinto ejercicio
sueldo = float(input("Digite el sueldo base del trabajador\n"))
ley_politica_publica = sueldo * 0.01
seguro_social = sueldo * 0.04
seguro_forzoso = sueldo * 0.005
caja_ahorro = sueldo * 0.05
total = sueldo - seguro_social - seguro_forzoso - caja_ahorro
print(f'''Descuentos:
Ley política pública: {ley_politica_publica}
Seguro social: {seguro_social}
Seguro forzoso: {seguro_forzoso}
Caja ahorro: {caja_ahorro}
Total a pagar: {total}''')

#Sexto ejercicio
palabras = int(input("Digite el número de palabras que contendrá el aviso\n"))
tamaño = float(input("Digite la cantidad (en cm) que tendrá el aviso\n"))
colores = int(input("Digite el número de colores que tendrá el aviso\n"))
total = (palabras*20000)+(tamaño*15000)+(colores*25000)
print(f"El total a cobrar por el aviso clasificado es: {total}")

#Séptimo ejercicio
años = int(input("Digite la cantidad de años que lleva el trabajador en la empresa\n"))-1
total = 100000 + (120000*años)
print(f"El monto por bono de antiguedad es: {total}")

#Octavo ejercicio
horas = int(input("Digite el número de horas que trabajó el profesor\n"))
pago = (20000*horas)
total = pago - (pago * 0.05)
print(f"El monto total a pagar al profesor es: {total}")

#Noveno ejercicio
inicial = float(input("Digite el monto inicial de la tarjeta\n"))
final = float(input("Digite el monto final de la tarjeta\n"))
consumido = inicial-final
recargo = consumido * 0.2
total = consumido + recargo
print(f"El total a cobrar al cliente es {total}")


#Décimo ejercicio
fotos = int(input("Digite el número de fotos a revelar\n"))
neto = fotos * 1500
total = neto + (neto * 0.16)
print(f"El monto total por el revelado (Incluyendo IVA DE 16%) es: {total}")

#Undécimo ejercicio
monto = float(input("Digite el monto presupuestal del hospital\n"))
gine = monto * 0.4
trauma = monto * 0.3
pedia = monto * 0.3
print(f'''Para el monto total {monto}
el área de ginecología recibirá {gine}
el área de traumatología recibirá {trauma}
y, el área de pediatría recibirá {pedia}''')

#Duodécimo ejercicio
cantidad = int(input("Digite la cantidad de películas a alquilar\n"))
dias = int(input("Digite la cantidad de días a alquilar la película\n"))
total = (1500*dias)*(cantidad-1)
print(f"El monto total a pagar por el alquiler de {cantidad} películas por {dias} días es: {total}")

#Décimo tercer ejercicio
cantidad = int(input("Digite la cantidad de personas que irán al tour de Cartagena\n"))
dias = int(input("Digite el número de días en los que la(s) persona(s) irá(n) al tour\n"))
neto = (25000*dias)*cantidad
total = neto + (neto*0.12)
print(f"El monto total a pagar por la familia al tour de Cartagena es: {total}")

#Décimo cuarto ejercicio
dias = int(input("Digite la cantidad de días que estarán los clientes en la habitación\n"))
total = (100000)+(200000*(dias-1))
print(f"El monto total a pagar es: {total}")

#Décimo quinto ejercicio
monto = float(input("Digite el monto del préstamo\n"))
interes = monto * (0.24)
total = monto + interes
especiales = (total*0.5)/4
ordinarias = (total*0.5)/20
print(f"El monto total a pagar por el préstamo es: {total}, el valor de las cuatro cuotas especiales es: {especiales} y el de las 20 {ordinarias}")


