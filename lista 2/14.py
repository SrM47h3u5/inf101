#crescente decrescente
x = int(input("Digite o primeiro valor (X): "))
y = int(input("Digite o segundo valor (Y): "))

opcao = int(input("Escolha a ordem: 1 para crescente, 2 para decrescente: "))

if opcao == 1:
    if x < y:
        print(f"Ordem crescente: {x}, {y}")
    else:
        print(f"Ordem crescente: {y}, {x}")
elif opcao == 2:
    if x > y:
        print(f"Ordem decrescente: {x}, {y}")
    else:
        print(f"Ordem decrescente: {y}, {x}")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")