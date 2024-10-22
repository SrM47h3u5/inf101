#par impar positivo negativo
n = int(input("Digite um número: "))

if n % 2 == 0:
    par_ou_impar = "par"
else:
    par_ou_impar = "ímpar"

if n > 0:
    sinal = "positivo"
elif n < 0:
    sinal = "negativo"
else:
    sinal = "zero"

print(f"O número é {par_ou_impar} e {sinal}.")