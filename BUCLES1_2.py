email = input("Ingrese una dirección de correo electrónico: ")

if email.count("@") == 1 and email.count(".") > 0:
    print("El correo electrónico es válido.")
else:
    print("El correo electrónico es inválido.")