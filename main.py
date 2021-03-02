#Liliana Esmeral
#taller condicionales Liliana Esmeral
#Punto 1

camisas = int(input("Digite el total de camisas compradas\n"))
neto = 0

for i in range(camisas):
    neto = neto + float(input(f"Digite el valor de la camisa #{i+1}\n$"))
if camisas >= 3:
    print(f"El valor total es: {neto-(neto*0.3)}")
else:
    print(f"El valor total es: {neto-(neto*0.1)}")


#Punto 2
total = float(input("Digite el total de la compra\n"))
numero = int(input("Digite el número al azar que le tocó al cliente\n"))
if numero < 74:
    print(f"El total a pagar por el cliente tiene un 15% de descuento, por lo tanto es: {total-(total*0.15)}")
else:
    print(f"El total a pagar por el cliente tiene un 20% de descuento, por lo tanto es: {total-(total*0.2)}")
    
#Punto 3
finanza = float(input("Digite el valor por el que se ejecuta la finanza\n"))
if finanza < 50000:
    print(f"La cuota a pagar es del 3% del monto: {finanza-finanza*0.03}")
elif finanza > 50000:
    print(f"La cuota a pagar es del 2% del monto: {finanza-finanza*0.02}")

#Punto 4
total = 0
ganancias = 0
for i in range(5):
    total = total + float(input(f"Digite los puntos de contaminación que emite la fábrica en el día {i+1} medido en la semana\n"))
    ganancias = ganancias + float(input(f"Digite la ganancia que se produjo el día {i+1} medido en la semana\n"))
promedio = total / 5
if promedio > 170:
    print(f'''La fábrica emite un promedio de {promedio},
por lo tanto tendrá la sanción de parar su producción por una semana
y una multa de {ganancias*0.5}''')
else:
    print(f"La fábrica tiene un promedio de {promedio}, por lo que no tiene sanción ni multa")


#Punto 5
precio = float(input("Digite el precio del terreno del terreno y auto\n"))
porc_deval = float(input("Digite el porcentaje (%) de devaluación del automovil\n"))
porc_val = float(input("Digite el porcentaje (%) de revalorización del terreno\n"))
revalorizacion = (precio*(porc_val/100)*3)
devaluacion = (precio*(porc_deval/100)*3)
print(f"El los precios de devaluación y revalorización respectivamente son: {devaluacion},{revalorizacion}")
if devaluacion < (revalorizacion/2):
    print("Se debe comprar el automovil debido a que la devaluación de este es menor que la mitad de la revalorización del terreno")
else:
    print("El precio de la devaluación es mayor o igual a la mitad de la revalorización del terreno, por lo que no es viable comprarlo.")

#Punto 6
unitario = 11000
cantidad = int(input("Digite el número de computadoras que se comprarán\n"))
neto = unitario*cantidad
if cantidad < 5:
    print(f"El valor total a pagar es: {neto-(neto*0.1)}")
elif cantidad >= 5 & cantidad < 10:
    print(f"El valor total a pagar es: {neto-(neto*0.2)}")
else:
    print(f"El valor total a pagar es: {neto-(neto*0.4)}")
    
#Punto 7
precio = float(input("Digite el precio del aparato a comprar\n"))
marca = input("Digite la marca del aparato a comprar\n")
precio_desc = precio
if precio >= 2000:
    precio_desc = precio_desc - (precio_desc * 0.1)
total = precio_desc + (precio_desc*0.16)
if marca == "NOSY":
    total = total - (total*0.05)
print(f"El monto total que debe pagar el cliente es: {total}")


#Punto 8
monto = float(input("Digite el monto total de la compra\n"))
if monto > 500000:
    propio = monto*0.55
    prestado = monto*0.3
    credito = monto*0.2
    interes = credito*0.2
    print(f'''La cantidad a invertir es: {propio}
el valor a pedir prestado al banco: {prestado}
el valor del crédito al fabricante: {credito}
y el interés del 20% del crédito: {interes}''')
else:
    propio = monto*0.7
    credito = monto*0.3
    interes = credito*0.2
    print(f'''La cantidad a invertir es: {propio}
el valor del crédito al fabricante: {credito}
y el interés del 20% del crédito: {interes}''')


#Punto 9
n1 = float(input("Digite el primer número"))
n2 = float(input("Digite el segundo número"))

if n1 == n2:
    print(n1*n2)
elif n1 > n2:
    print(n1-n2)
else:
    print(n1+n2)


#Punto 10
n1 = float(input("Digite el primer número\n"))
n2 = float(input("Digite el segundo número\n"))
n3 = float(input("Digite el tercer número\n"))

if (n1 > n2) & (n1 > n3):
    print(f"El mayor es {n1}")
elif (n2 > n1) & (n2 > n3):
    print(f"El mayor es {n2}")
elif (n3 > n1) & (n3 > n2):
    print(f"El mayor es {n3}")
else:
    print("Los números son iguales")

