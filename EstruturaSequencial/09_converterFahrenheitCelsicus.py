# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

fanhrenheit = float(input("Informe a temperatura em graus Fahrenheit: "))
celsius = 5 * ((fanhrenheit - 32) / 9)

print(str(fanhrenheit) +"ºF equivalem a " + str(round(celsius, 2)) + "ºC")