# 3) Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro. Escreva um programa em Python que pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False) e quantas vezes venceu um jogo. O programa deve imprimir True, permitindo o ingresso do participante no clube, se:
# tiver entre 16 e 18 anos
# já tiver jogado pelo menos 3 jogos
# já ter vencido pelo menos 1 jogo

idade = int(input("Digite sua idade: "))
jogos = input("Você já jogou pelo menos 3 jogos de tabuleiro? (Responda True pra sim e False pra não) : ")
win = int(input("Quantos jogos você já venceu? : "))
apto = (idade > 15 and idade < 19) and jogos == 'True' and win > 0
print(apto)