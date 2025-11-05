
#a un empleado le aplican una retencion del 18% sobre su salario basico, y le entregan una bonificacion del 1.3% sobre el salario. desarrolle un algoritmo que permita calcular e imprimir el salario neto y los valores de sus respectivos porcentajes.
salario_basico = float(input("Ingrese su salario básico: "))
retencion = salario_basico * 0.18
bonificacion = salario_basico * 0.013
salario_neto = salario_basico - retencion + bonificacion

print("Retención:", retencion)
print("Bonificación:", bonificacion)
print("Salario neto:", salario_neto)

#area de la cancha
area = float(input("Ingrese el área de la cancha: "))
nueva_area = area * 1.20
print("El área total después de ampliarla es:", nueva_area)

#desempleo actual 
desempleo = float(input("Ingrese el valor inicial del desempleo: "))
primer_trimestre = desempleo * 1.095
segundo_trimestre = primer_trimestre * 0.985
print("El desempleo actual es:", segundo_trimestre)


#area total de un terreno
area = float(input("Ingrese el área del terreno: "))
area_reducida = area * 0.90
area_final = area_reducida * 1.50
print("El área total final del terreno es:", area_final)


#minutos a horas 
minutos = float(input("Ingrese los minutos: "))
horas = minutos / 60
print("Equivale a", horas, "horas")


#horas a minutos
horas = float(input("Ingrese las horas: "))
minutos = horas * 60
print("Equivale a", minutos, "minutos")


#quilates a kilos 
quintales = float(input("Ingrese la cantidad en quintales: "))
kilogramos = quintales * 100
print("Equivale a", kilogramos, "kilogramos")


#costo de llamadas 
llamada1 = float(input("Costo llamada 1 operador 1: "))
llamada2 = float(input("Costo llamada 2 operador 1: "))
llamada3 = float(input("Costo llamada 1 operador 2: "))
llamada4 = float(input("Costo llamada 2 operador 2: "))

total_op1 = llamada1 + llamada2
total_op2 = llamada3 + llamada4
total_general = total_op1 + total_op2

print("Total operador 1:", total_op1)
print("Total operador 2:", total_op2)
print("Total de las cuatro llamadas:", total_general)


#area de baño y las cajas de las baldosas 
alto = float(input("Ingrese el alto del muro: "))
ancho = float(input("Ingrese el ancho del muro: "))
area = alto * ancho
cajas = area / 3.5
print("Área del baño:", area)
print("Cajas necesarias:", cajas)


#tiempo y distancia 
t1 = float(input("Tiempo día 1: "))
t2 = float(input("Tiempo día 2: "))
t3 = float(input("Tiempo día 3: "))
d1 = float(input("Distancia día 1: "))
d2 = float(input("Distancia día 2: "))
d3 = float(input("Distancia día 3: "))

total_tiempo = t1 + t2 + t3
total_distancia = d1 + d2 + d3
prom_tiempo = total_tiempo / 3
prom_distancia = total_distancia / 3

print("Tiempo total:", total_tiempo)
print("Distancia total:", total_distancia)
print("Promedio de tiempo:", prom_tiempo)
print("Promedio de distancia:", prom_distancia)


#herencia
total = float(input("Ingrese el valor total de la herencia: "))

esposa = total * 0.40
hijo1 = total * 0.30
hijo2 = total * 0.20
hijo3 = total * 0.40
hijo4 = total * 0.10

print("Esposa:", esposa)
print("Hijo 1:", hijo1)
print("Hijo 2:", hijo2)
print("Hijo 3:", hijo3)
print("Hijo 4:", hijo4)


#terreno para los proyectos 
area_total = float(input("Ingrese el área total del terreno: "))

cultivos = area_total * 0.40
vivienda = area_total * 0.25
zonas_verdes = area_total * 0.15
disponible = area_total - (cultivos + vivienda + zonas_verdes)

print("Cultivos:", cultivos)
print("Vivienda:", vivienda)
print("Zonas verdes:", zonas_verdes)
print("Área disponible:", disponible)


#nota definitiva 
t1 = float(input("Taller 1: "))
t2 = float(input("Taller 2: "))
prom_talleres = (t1 + t2) / 2

e1 = float(input("Evaluación 1: "))
e2 = float(input("Evaluación 2: "))
e3 = float(input("Evaluación 3: "))
prom_evaluaciones = (e1 + e2 + e3) / 3

trabajo_final = float(input("Nota trabajo final: "))

q1 = float(input("Quiz 1: "))
q2 = float(input("Quiz 2: "))
q3 = float(input("Quiz 3: "))
q4 = float(input("Quiz 4: "))
prom_quiz = (q1 + q2 + q3 + q4) / 4

nota_final = (prom_talleres * 0.15) + (prom_evaluaciones * 0.30) + (trabajo_final * 0.30) + (prom_quiz * 0.25)

print("Nota definitiva:", nota_final)


#liquidacion 
inicio = int(input("Número inicial de la registradora: "))
final = int(input("Número final de la registradora: "))
valor_pasaje = float(input("Valor del pasaje: "))

pasajeros = final - inicio
total_dinero = pasajeros * valor_pasaje
empresa = total_dinero * 0.75
conductor = total_dinero * 0.25

print("Total pasajeros:", pasajeros)
print("Total liquidado:", total_dinero)
print("Empresa recibe:", empresa)
print("Conductor recibe:", conductor)

