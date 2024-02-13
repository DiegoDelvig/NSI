# Diego Delvig 1G7


def binversdec(binaire: str) -> int:
	"""
	Retourne la valeur decimal du nombre binaire passé en paramétre
	"""

	n = len(binaire)
	decimal = 0

	for i in range(n):
		decimal = decimal + int(binaire[n - 1 - i]) * 2 ** i

	return decimal


def decversbin(decimal: int) -> str:
	"""
	Retourne la valeur binaire du nombre decimal passé en paramétre
	"""
	
	reste = ''
	while decimal >= 1:
		
		reste = str(decimal % 2) + reste 
		decimal = decimal // 2		

	return reste



mode = input('convertir en dec ou bin: ')

if mode == 'dec':
	demande = input('binaire -> decimal ')
	print(demande, ' -> ', binversdec(demande))

elif mode == 'bin':
	demande = int(input('decimal -> binaire '))
	print(demande, ' -> ', decversbin(demande))

else:
	print("Reponse inconnue")
