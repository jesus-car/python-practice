def palindromo(frase):
	frase=frase.replace(" ", "")
	return frase==frase[::-1]

frase="anita lava la tina"
resultado=palindromo(frase)
print(resultado)