pago_total=int(input("Ingrese cuanto quiere pagar:\n"))

lectura_anterior=int(input("Ingrese la ultima lectura del medidor:\n "))

kwh=0.6673

pago_final=(pago_total/1.18)-10

lectura_actual=lectura_anterior+(pago_final/kwh)

consumo_mes=lectura_actual-lectura_anterior

print("Su consumo debe ser: ", int(consumo_mes))
print("Su lectura final debe ser: ", int(lectura_actual))