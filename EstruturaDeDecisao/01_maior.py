# Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input("Informe o 1º número: "))
n2 = int(input("Informe o 2º número: "))

if n1 > n2:
    print(str(n1) + " é o maior número digitado")
elif n2 > n1:
    print(str(n2) + " é o maior número digitado")
else:
    print("Os números são iguais")
