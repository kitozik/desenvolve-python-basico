n = int(input("Digite a quantidade de números: "))

maior = 0

while n > 0:
    x = int(input("Digite um número: "))
    if x > maior:
        maior = x
        n -= 1
    else:
        n -= 1

print(f'{maior} é o maior desses números')