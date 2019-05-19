soma = 0
x = 0
numero = 0
while True:
	numero = float(input("Informe um Numero ou 0 para sair: "))
	if numero == 0:
		break
	soma += numero
	x += 1
print ("A Soma e = %3.2f e a Media = %3.2f "%(soma,(soma/x)))
