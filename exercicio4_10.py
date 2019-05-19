consumo = float(input("Informe Consumo em kWh: "))
tipo = input("Informe Tipo [R=Residencial C=Comercial I=Industrial]: ")
if tipo == "R":
    if consumo <= 500:
        print("O Comuso e = R$%5.2f "%(consumo*0.40))
    else:
        print("O Comuso e = R$%5.2f "%(consumo*0.65))
elif tipo <= "C":
    if consumo <= 1000:
        print("O Comuso e = R$%5.2f "%(consumo*0.55))
    else:
        print("O Comuso e = R$%5.2f "%(consumo*0.60))
elif tipo == "I":
    if consumo <= 5000:
        print("O Comuso e = R$%5.2f "%(consumo*0.55))
    else:
        print("O Comuso e = R$%5.2f "%(consumo*0.60))
else:
    print("Informacao Incorreta")
    
