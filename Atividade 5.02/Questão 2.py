n1 = int(input("Informe um número:"))
n2 = int(input("Informe um número:"))
n3 = int(input("Informe um número:"))

maior = n1
menor = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print("O maior eh:",maior,"\n e o menor:",menor)    