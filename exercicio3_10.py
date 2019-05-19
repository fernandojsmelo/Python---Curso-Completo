salario = int(input("Informe Salario: "))
reajuste = int(input("Informe almento: "))
vlreajuste = 0
vlreajuste = (salario*reajuste)/100
salario = salario + (salario*reajuste)/100
print("O Reajuste do Salario e R$ %5.2f e o Salario ficou R$ %5.2f"
	%(vlreajuste,salario))
