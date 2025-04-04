# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input("Informe o 1º número: "))
n2 = int(input("Informe o 2º número: "))
n3 = int(input("Informe o 3º número: "))

if n1 == n2 and n1 == n3:
    print("Números repetidos")
elif n1 == n2 and n1 > n3:
    print(str(n1) + " se repete e é o maior " + str(n3) + " é o menor")
elif n1 == n3 and n1 > n2:
    print(str(n1) + " se repete e é o maior " + str(n2) + " é o menor")
elif n2 == n3 and n2 > n1:
    print(str(n2) + " se repete e é o maior " + str(n3) + " é o menor")
elif n1 == n2 and n1 < n3:
    print(str(n1) + " se repete e é o menor " + str(n3) + " é o maior")
elif n1 == n3 and n1 < n2:
    print(str(n1) + " se repete e é o menor " + str(n2) + " é o maior")
elif n2 == n3 and n2 < n1:
    print(str(n2) + " se repete e é o menor " + str(n3) + " é o maior")
elif n1 != n2 and n1 != n3 and n2 != n3:
    if (n1 > n2 and n1 > n3) and (n2 < n1 and n2 < n3):
        print("Maior: " + str(n1) + " Menor: " + str(n2))
    elif (n1 > n2 and n1 > n3) and (n3 < n1 and n3 < n2):
        print("Maior: " + str(n1) + " Menor: " + str(n3))
    elif (n2 > n1 and n2 > n3) and (n1 > n2 and n1 < n3):
        print("Maior: " + str(n2) + " Menor: " + str(n1))
    elif (n2 > n1 and n2 > n3) and (n3 < n1 and n3 < n2):
        print("Maior: " + str(n2) + " Menor: " + str(n1))
    elif (n3 > n1 and n3 > n2) and (n1 < n2 and n1 < n3):
        print("Maior: " + str(n3) + " Menor: " + str(n1))
    elif (n3 > n1 and n3 > n2) and (n2 < n1 and n2 < n3):
        print("Maior: " + str(n3) + " Menor: " + str(n2))