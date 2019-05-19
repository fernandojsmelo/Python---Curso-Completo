dp_inicio = float(input("Informe deposito : "))
tx_juros  = float(input("Informe taxa de juros : "))
x = 1
juros = 0
ganho = 0
while x <= 24:
        juros = (dp_inicio*(tx_juros)/100)
        dp_inicio += juros
        ganho += juros
        print("Mes %d Ganho com Juros = %3.2f e o redimento = %5.2f"
              %(x,ganho,dp_inicio))
        x = x + 1
