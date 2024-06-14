# Você é mestre de uma mesa de RPG e vai criar um sistema para validar uma ficha de personagem. Cada personagem tem uma classe específica com requisitos de atributos. Escreva um script que solicita a classe de personagem escolhida (guerreiro, mago ou arqueiro), os pontos de força e os pontos de magia atribuídos ao personagem. O programa deve imprimir True se os pontos de atributo são consistentes com a classe escolhida, seguindo as seguintes regras:
# Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.
# Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.
# Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles pode ser superior a 15.

classe = input("Digite a classe escolhida: ")
força = int(input("Digite seu nível de força (1 a 20): "))
magia = int(input("Digite seu nível de magia: (1 a 20): "))

guerreiro = classe == 'guerreiro' and força >= 15 and magia <= 10
mago = classe == 'mago' and força <= 10 and magia >= 15
arqueiro = classe == 'arqueiro' and força > 5 and força < 16 and magia >  5 and magia < 16

atributos = arqueiro or mago or guerreiro

print("Pontos de atributo consistentes com a classe escolhida:", atributos )