# 1) Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar. Lembre-se do operador do python % que retorna o resto de uma divisão.
a = int(input("Digite um número: "))
b = int (input("Digite outro número: "))

soma = a + b

numero = soma%2

if numero == 0:
    print("A soma dos números é par")
else:
    print("A soma dos números é ímpar")  