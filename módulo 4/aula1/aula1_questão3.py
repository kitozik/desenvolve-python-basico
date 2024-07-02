n1= int(input("Digite sua nota: "))
n2= int(input("Digite sua nota: "))
n3= int(input("Digite sua nota: "))

m = (n1 + n2 + n3)/3

if m>=60:
    print("Aprovado!")
elif m >= 40:
    print("Recuperação.")
else:
    print("Reprovado.")

print("FIM")
