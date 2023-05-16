while True:
    nota = input("Ingrese la nota: ")
    
    if nota.isnumeric():
        nota = int(nota)
        if nota < 5:
            print("Desaprobado")
            break
        elif nota >= 5 and nota <= 10:
            print("Aprobado")
            break
        elif nota > 10:
            print("El valor es inválido, ingrese la nota de nuevo")
    else:
        print("El valor es inválido, ingrese la nota de nuevo")