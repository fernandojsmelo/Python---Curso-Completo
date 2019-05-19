a = int(input("Informe o Primeiro Numero: "))
b = int(input("Informe o Segndo Numero: "))
c = int(input("Informe o Terseiro Numero: "))
maior = 0
menor = 0
if a > b and a > c:
    mairo = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
if a < b and a < b:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print("O maior = %d e Menor = %d " % (maior,menor))
