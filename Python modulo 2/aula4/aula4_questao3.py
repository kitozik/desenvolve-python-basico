nome_produto1 = input(f"Digite o nome do produto1: ")
preço_unit = float(input("Digite o preço da unidade do produto1: "))
quantidade = int(input("Digite a quantidade do produto: "))
nome_produto2 = input(f"Digite o nome do produto2: ")
preço_unit2 = float(input("Digite o preço da unidade do produto: "))
quantidade2 = int(input("Digite a quantidade do produto: "))
nome_produto3 = input(f"Digite o nome do produto3: ")
preço_unit3 = float(input("Digite o preço da unidade do produto: "))
quantidade3 = int(input("Digite a quantidade do produto: "))

total = (preço_unit * quantidade) + (preço_unit2 * quantidade2) + (preço_unit3 * quantidade3)

print(f"Total: R${total:.2f}")