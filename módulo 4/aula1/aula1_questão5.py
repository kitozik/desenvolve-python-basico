n = int(input("Digite a quantidade de pessoas: "))

maior = 0
soma = 0
while n > 0:
    x = int(input("Digite uma idade: "))
    soma += x
    if x > maior:
        maior = x
        n -= 1
    else:
        n -= 1

media = soma/3
print(f'{media: .0f} anos é a média de idade')