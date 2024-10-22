#operadores
operador = input("Digite um operador (+,-,*,/): ")
n1 = int(input("Digite um  numero: "))
n2 = int(input("Digite mais um numero: "))
if operador == '+':
    resultado1 = (n1 + n2)
    print("o valor da adição será de:", resultado1)
elif operador == "-":
    resultado2 = (n1 - n2)
    print(f"o valor da subtração será de: {resultado2}")
elif operador == "*":
    resultado3 = (n1 * n2)
    print(f"O valor da multiplicação será de: {resultado3}")
elif operador == "/":
    if n2 != 0:
        resultado4 = (n1 / n2)
        print(f"O valor da divisão será de: {resultado4}")
    else:
        print("Divisão por zero não permitida")
else:
    print("operador inálido digite (+,-,*,/)")