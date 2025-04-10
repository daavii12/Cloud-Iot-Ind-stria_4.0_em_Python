nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media =(nota1 + nota2)/2
print(media)
if media >= 7:
    print("Aprovado (a)")
elif media == 6:
    print("Recuperação")
else:
    print("Reprovado (a)")