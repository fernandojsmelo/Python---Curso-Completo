mercadoria = int(input("Informe o Valor da Mercadoria: "))
desconto = int(input("Informe o valor do desconto: "))
vldesconto = (mercadoria*desconto)/100
mercadoria = mercadoria -(mercadoria*desconto)/100
print("O Desconto foi R$ %3.2f e volar a Pagar e R$ %5.2f"
      %(vldesconto,mercadoria))
