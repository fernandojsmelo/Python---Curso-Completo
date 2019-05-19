a = float(input("Informe um Numero: "))
b = float(input("Informe outro Numero: "))
op = input("Iforme Operacao [+ - * /]: ")
if op == "+":
    print("Resultado = %3.2f"%(a+b))
elif op == "-":
    print("Resultado = %3.2f"%(a-b))
elif op =="*":
    print("Resultado = %3.2f"%(a*b))
elif op == "/":
    print("Resultado = %3.2f"%(a/b))
else:
    print("Informe incorreta")
