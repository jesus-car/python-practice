correo=input("Ingrese su correo: ")

email=False

for i in correo:
	
	if i == "@" :
		email=True

if email==True:
	print("El email es correcto")

else:
	print("Email incorrecto")

