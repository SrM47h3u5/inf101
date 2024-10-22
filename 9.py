# volume e areo cilindro
import math
r = int(input('Digite o valor do raio em cm: '))
h = int(input('Digite o valor da altura em cm: '))

area =  int((r*r) * math.pi)
volume =  int(math.pi*r**2*h)

print (f"A área do triângulo é: {area} cm²" )
print(f"O volume do triangulo é: {volume} cm³")