hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

y=mins+dura

a=y%60
b=hour+y//60
c=b%24

print(c,":",a)
