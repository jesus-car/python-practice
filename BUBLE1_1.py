contador=0
contador1=0

email=input("Ingrese su email: ")

for i in email:

	if i=="@":
		contador=contador+1

for i in email:

	if i ==".":
		contador1=contador1+1

if contador==1 and contador1>0:
	print("El email es correcto")

else:
	print("Email incorrecto")

