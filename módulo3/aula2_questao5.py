# Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:
# A: Para mulheres, ter mais de 60 anos. Para homens, 65.
# B: Ou ter trabalhado pelo menos 30 anos
# C: Ou ter 60 anos  e trabalhado pelo menos 25.

genero = input("Digite seu gênero (m ou f): ")
idade = int(input("Digite sua idade: "))
tempo_trabalho = int(input("Digite seu tempo de trabalho: "))
homens = genero == 'm' and idade > 65 or tempo_trabalho >= 30 or (idade >= 60 and tempo_trabalho >= 25)
mulheres = genero == 'f' and idade > 65 or tempo_trabalho >= 30 or (idade >= 60 and tempo_trabalho >= 25)

print("Requerimentos para apostentar :", homens or mulheres)
