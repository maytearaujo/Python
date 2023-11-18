# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("Informe sua altura: "));
genero = input("Informe seu gênero: \nF - Feminino | M - Masculino:\n")

if genero == 'M' or 'm':
    pesoIdeal = (72.7*altura) - 58;
else:
    pesoIdeal = (62.1*altura) - 44.7;


print("O seu peso ideal é: "+ str(round(pesoIdeal)) + " kg");