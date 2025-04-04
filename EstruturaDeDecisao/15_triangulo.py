# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

a = int(input("Informe o 1º lado: "))
b = int(input("Informe o 2º lado: "))
c = int(input("Informe o 3º lado: "))

if (a + b) > c or (b + c) > a or (a + c) > b:
    if a == b and b == c:
        print("Triângulo Equilátero")
    elif a == b or a == c or b == c:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')
else:
    print("Os lados não formam um triângulo")