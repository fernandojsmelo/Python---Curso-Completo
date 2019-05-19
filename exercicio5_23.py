n = float(input("Informe um Numero: "))
div = 0
if (n%2 == 0):
    m = n
while m != 0:
    div = n / m
    if  div == 0:
        print("O Numero Nao eh Primo")
        break
    else:
        print("O Numero Eh Primo")
    m -= 1
