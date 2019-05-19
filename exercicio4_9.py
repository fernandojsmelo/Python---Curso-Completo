vcasa = float(input("Informe o Valor da Casa R$: "))
vsalario = float(input("Informe o Valor do Salario R$: "))
qanos = float(input("Informe em Quantos Anos para Pagar: "))
vprest = 0
vminimo = (vsalario * 0.30)
nmes = (qanos * 12)
vprest = (vcasa/nmes)
if vprest <= vminimo:
    print("O valor da Pestacao e R$ %5.3f "%vprest)
else:
    print("Valor da Prestacao superior a 30% do Salario")
