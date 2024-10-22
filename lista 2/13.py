#presenca e media
presencas = int(input("Digite o número de presenças: "))

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1+n2+n3+n4)/4

if media > 6 and presencas >= 20:
    print("APROVADO")
elif 5 <= media < 6 and presencas >= 20:
    print("DEPENDÊNCIA")
else:
    print("REPROVADO")
