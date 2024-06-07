comprimento = int(input("Digite o comprimento do terreno: "))
largura = int(input("Digite a largura do terreno: "))
area = int(comprimento * largura)
print(f"A área do terreno é de {area}m²")
preço = float(input("Digite o preço do m² da região: "))
preçom2 = preço * area
print(f"O terreno possui {area}m² e custa R${preçom2:,.2f}.")