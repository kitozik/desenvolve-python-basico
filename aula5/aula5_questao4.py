# 4) Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
# Distância até 100 km: R$1 por kg.
# Distância entre 101 e 300 km: R$1.50 por kg.
# Distância acima de 300 km: R$2 por kg.
# Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

distancia = int(input("Digite a distância desejada em km: "))
peso = int(input("Digite o peso da carga em KG: "))
preço = ()

if distancia <= 100:
    preço = 1 * peso
    if peso > 10:
        preço += 10
elif distancia <= 300:
    preço = 1.5 * peso
    if peso > 10:
        preço += 10
elif distancia > 300:
    preço = 2 * peso
    if peso > 10:
        preço += 10

print(f'O preço do frete ficará em R${preço:.2f} reais')