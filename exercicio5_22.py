def menu():
	print(" 1 : Adicao \n 2 : Subtracao \n 3 : Divisao \n 4 : Multiplicacao \n 5 : Sair \n")
	m = int(input("\n"))
	if (m >= 6):
		prit("Operacao Invalida\n \n")
		menu()
	elif (m <= 0):
		prit("Operacao Invalida\n \n")
		menu()
	elif (m == 1):
		soma()
	elif (m == 2):
		subtracao()
	elif (m == 3):
		divisao()
	elif (m == 4):
		multiplicacao()
	elif (m == 5):
		exit

def soma():
	x = int(input("Informe o Primeiro Numero : "))
	y = int(input("Informe o Segundo Numero :"))
	print("A Soma dos Dois Numeros = %d"%(x+y))
	i = int(input(" 1 : Outra Soma \n 2 : Voltar ao Menu Principal \n 3 : Sair do Programa \n"))
	if (i == 1):
		soma()
	elif (i == 3):
		exit
	else:
		menu()

def subtracao():
	a = int(input("Informe o Primeiro Numero : "))
	b = int(input("Informe o Segundo Numero : "))
	c = a - b
	print("A Subtracao dos Dois Numeros = %d"%c)
	i = int(input(" 1 : Outra Subtracao \n 2 : Voltar ao Menu Principal \n 3 : Sair do Programa \n"))
	if (i == 1):
		subtracao()
	elif (i == 3):
		exit
	else:
		menu()

def divisao():
	a = int(input("Informe o Primeiro Numero : "))
	b = int(input("Informe o Segundo Numero : "))
	c = a / b
	print("A Divisao dos Dois Numeros = %d"%c)
	i = int(input(" 1 : Outra Divisao \n 2 : Voltar ao Menu Principal \n 3 : Sair do Programa \n"))
	if (i == 1):
		divisao()
	elif (i == 3):
		exit
	else:
		menu()

def multiplicacao():
	a = int(input("Informe o Primeiro Numero : "))
	b = int(input("Informe o Segundo Numero : "))
	c = a * b
	print("A Multiplicacao dos Dois Numeros = %d"%c)
	i = int(input(" 1 : Outra Multiplicacao \n 2 : Voltar ao Menu Principal \n 3 : Sair do Programa \n"))
	if (i == 1):
		multiplicacao()
	elif (i == 3):
		exit
	else:
		menu()
menu()