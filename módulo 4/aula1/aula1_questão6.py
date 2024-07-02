n = int(input("Digite a quantidade de experimentos: "))
cont = 0
total = 0
total_s = 0
total_r = 0
total_c = 0
while cont < n:
    quantia = int(input("Digite a quantia da especie que está sendo utilizada: "))
    especie = input("Digite a especie utilizada (S: Sapo, R: Rato ou C: Coelho): ")
    cont +=1
    total += quantia
    if especie == "S":
        total_s += quantia
    elif especie == "R":
        total_r += quantia
    elif especie == "C":
        total_c += quantia

print(f'Total de cobaias usadas: {total}')
print(f'Total de sapos usadas: {total_s}')
print(f'Total de ratos usadas: {total_r}')
print(f'Total de coelhos usadas: {total_c}')

print(f'Pecentual de sapos: {total_s * 100 /total: .2f}%')
print(f'Pecentual de ratos: {total_r * 100 /total: .2f}%')
print(f'Pecentual de coelhos: {total_c * 100 /total: .2f}%')