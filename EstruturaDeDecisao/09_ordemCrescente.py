#Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int(input("Informe o 1º número: "))
n2 = int(input("Informe o 2º número: "))
n3 = int(input("Informe o 3º número: "))

if n1 == n2 and n1 == n3:
    print("números iguais")
elif n1 != n2 and n1 != n3:        
    if n1 > n2 and n1 > n3:
        maior = n1
        if n2 > n3:
            medio = n2
            menor = n3
        else:
            medio = n3
            menor = n2
            
            
    if n2 > n1 and n2 > n3:
        maior = n2
        if n1 > n3:
            medio = n1
            menor = n3
        else:
            medio = n3
            menor = n1
            
            
    if n3 > n1 and n3 > n2:
        maior = n3
        if n1 > n2:
            medio = n1
            menor = n2
        else:
            medio = n2
            menor = n1
            
            
    
print(f'{maior}, {medio}, {menor}')
