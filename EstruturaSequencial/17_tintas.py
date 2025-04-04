# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area = float(input("Informe a área a ser pintada (m²): "))

litrosNecessarios = area / 6
# latas18 = litrosNecessarios / 18
# latas3_6 = litrosNecessarios / 3.6

if ( litrosNecessarios % 18 == 0):
    latas = litrosNecessarios / 18
    precoTotal = latas * 80
    print("latas de tinta a serem compradas: " + str(round(latas)) + " lata(s) de 18L\n + Preço Total: "+str(round(precoTotal)))


elif(litrosNecessarios % 3.6 == 0):
    latas = litrosNecessarios / 3.6
    precoTotal = latas * 25
    print("latas de tinta a serem compradas: " + str(round(latas)) + " lata(s) de 3,6L\n + Preço Total: "+str(round(precoTotal)))


else:
    if(litrosNecessarios > 18):
        latas18 = litrosNecessarios // 18
        resto = litrosNecessarios % 18
        
        preco18 = latas18 * 80

        latas3_6 = resto / 3.6
        preco3_6 = latas3_6 * 25

        precoTotal = preco18 + preco3_6;
        
        print("latas de tinta a serem compradas: " + str(round(latas18)) + " latas de 18L e " + str(round(latas3_6)) + " latas de 3.6L \nPreço Total: "+str(round(precoTotal)))