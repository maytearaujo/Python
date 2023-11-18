# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

primeiro = int(input("Informe o 1º número inteiro: "))
segundo = int(input("Informe o 2º número inteiro: "))
terceiro = float(input("Informe um número real: "))

produto = (primeiro * 2) * (segundo / 2)
soma = (primeiro * 3) + terceiro
cubo = terceiro * terceiro * terceiro

print("o produto do dobro do primeiro com metade do segundo: " + str(produto))
print("a soma do triplo do primeiro com o terceiro: " + str(soma))
print("o terceiro elevado ao cubo: " + str(cubo))