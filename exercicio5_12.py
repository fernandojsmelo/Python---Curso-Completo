dp_inicio = float(input("Informe deposito : "))
tx_juros  = float(input("Informe taxa de juros : "))
x = 1
juros = 0
ganho = 0
while x <= 24:
        juros = (dp_inicio*(tx_juros)/100)
        dp_inicio += juros
        dp_mes = float(input("Informe Deposito Mensal: "))
        dp_inicio += dp_mes
        ganho += juros
        print("Mes %d Ganho com Juros = %3.2f e o redimento = %5.2f"
              %(x,ganho,dp_inicio))
        x = x + 1
