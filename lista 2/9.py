

passagem = 100.00
desconto = 20.00

idade = int(input("Digite sua idade: "))

if idade > 65 or idade < 18:
    valor_final = passagem - desconto
    print(f"Você tem direito ao desconto de R$ {desconto:.2f}.")
    print(f"Valor a ser pago pela passagem: R$ {valor_final:.2f}")
else:
    valor_final = passagem
    print("Você não tem direito ao desconto.")
    print(f"Valor a ser pago pela passagem: R$ {valor_final:.2f}")