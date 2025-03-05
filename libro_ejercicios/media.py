resultado = 0
numero_iteraciones = 0


def obtener_numero():
	numero = float(input("Numero: "))
	return numero


def casting_numbers(num):
	if num % 1 != 0:
		num = float(num)
	elif num % 1 == 0:
		num = int(num)
	return num

def calc_media(numero_sumado, numero_iteraciones):
	return numero_sumado / numero_iteraciones


while True:
	try:
		numero = obtener_numero()
		if numero == 0:
			print()
			print(f"Suma de los numeros: {resultado}")
			print(f"Media: {media}")
			break
		else:
			numero = casting_numbers(numero)
			numero_iteraciones += 1
			resultado += numero
			media  = calc_media(resultado,numero_iteraciones)
			print(f"Media de {resultado}: {media}")
	except Exception as error:
		print(f"Solamente se pueden ingresar numeros")
		print(error)
		break



