# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input("Informe o preço do 1º orçamento: "))
p2 = float(input("Informe o preço do 2º orçamento: "))
p3 = float(input("Informe o preço do 3º orçamento: "))

if p1 == p2 and p1 == p3:
    print("Os orçamentos são iguais")
elif p1 != p2 and p1 != p3 and p2 != p3:    
    if p1 < p2 and p1 < p3:
        print("O primeiro orçamento possui o menor preço: R$ " + str(p1))
    elif p2 < p1 and p2 < p3:
        print("O segundo orçamento possui o menor preço: R$ " + str(p2))
    elif p3 < p1 and p3 < p2:
        print("O terceiro orçamento possui o menor preço: R$ " + str(p3))
elif (p1 == p2 and p1 < p3) or (p2 == p1 and p2 < p3):
    print("O primeiro e segundo orçamento são iguais e possuem o menor preço: R$ " + str(p1))
elif p1 == p3 and p1 < p2:
    print("O primeiro e terceiro orçamento são iguais e possuem o menor preço: R$ " + str(p1))
elif p1 == p2 and p3 < p1:
    print("O terceiro orçamento possui o menor preço: R$ " + str(p3))
elif p2 == p3 and p2 < p1:
    print("O segundo e terceiro orçamento são iguais e possuem o menor preço: R$ " + str(p2))
elif p2 == p3 and p1 < p2:
    print("O primeiro orçamento possui o menor preço: R$ " + str(p1))
