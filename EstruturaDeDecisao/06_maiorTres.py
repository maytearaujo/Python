# Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input("Informe o 1º número: "))
n2 = int(input("Informe o 2º número: "))
n3 = int(input("Informe o 3º número: "))

if n1 == n2 and n1 == n3 and n2 == n3:
    print("Números repetidos")
elif n1 != n2 and n1 != n3 and n2 != n3:
    if n1 > n2 and n1 > n3:
        print(str(n1) + " é o maior número digitado")
    elif n2 > n1 and n2 > n3:
        print(str(n2) + " é o maior número digitado")
    elif n3 > n2 and n3> n1:
        print(str(n3) + " é o maior número digitado")
else:
    if n1 == n2 and n1 > n3:
        print("O número " +str(n1) + " se repete e é o maior entre os números digitados")
    elif n1 == n3 and n1 > n2:
        print("O número " +str(n1) + " se repete e é o maior entre os números digitados")
    elif n2 == n3 and n2 > n1:
        print("O número " +str(n2) + " se repete e é o maior entre os números digitados")
    elif n1 == n2 and n1 < n3:
        print(str(n3) + " é o maior número digitado")
    elif n1 == n3 and n1 < n2:
        print(str(n2) + " é o maior número digitado")
    elif n2 == n3 and n2 < n1:
        print(str(n1) + " é o maior número digitado")
