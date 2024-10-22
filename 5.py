n1 = int(input("Digite um numero:"))
n2 = int(input("digite mais um numero:"))

soma = n1+n2
diferença = n1-n2
multiplicaçao = n1*n2 
divisao = n1/n2 if n2 !=0 else "n2=0 divisao nao acontece "

print(f"A soma entre n1 e n2 é:  {soma}")
print(f"A diferença entre n1 e n2 é:  {diferença}")
print(f"A multiplicaçao entre n1 e n2 é:  {multiplicaçao}")
print(f"A divisao entre n1 e n2 é:  {divisao}")