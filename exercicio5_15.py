PD = 0
QT = 0
total = 0
while True:
	PD = int(input("Informe Codigo do Produto ou 0 para Sair: "))
	if PD == 0:
		break
	QT = float(input("Informe Quantidade desejada: "))
	
	if PD == 1:
		total += (0.50 * QT)
	elif PD == 2:
		total += (1.00 * QT)
	elif PD == 3:
		total += (4.00 * QT)
	elif PD == 5:
		total += (7.00 * QT)
	elif PD == 9:
		total += (8.00 * QT)
	else:
		print("Codigo Invalido")
		break
print("O Total das Compras = R$ %4.2f"%total)
