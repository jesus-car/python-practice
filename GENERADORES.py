def GeneraPares(limite):

	num=1

	miLista=[]

	while num<limite:
		miLista.append(num*2)

		num+=1

	return miLista

print(GeneraPares(5))


def GeneraPares2(limite):

	num=1

	while num<limite:

		yield num*2

		num=num+n1

devuelvePares=GeneraPares(10)

print(devuelvePares)