
operador = input("Digite um operador (+,-,*,/): ")
n1 = int(input("Digite um  numero: "))
n2 = int(input("Digite mais um numero: "))

match operador:
    case "+":
        resultado = (n1 + n2)
    case "-":
        resultado = (n1 - n2)
    case "*":
        resultado = (n1 * n2)
    case "/":
        resultado = (n1 / n2)
    case "_":
        print("operador inválido")
print("resultado:", resultado)