# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

from unittest import case


diaSemana = int(input("Informe o dia da semana: "))

if diaSemana == 1:
    print("Domingo");
elif diaSemana == 2:
    print("Segunda feira")
elif diaSemana == 3:
    print("Terça feira")
elif diaSemana == 4:
    print("Quarta feira")
elif diaSemana == 5:
    print("Quinta feira")
elif diaSemana == 6:
    print("Sexta Feira")
elif diaSemana == 7:
    print("Sábado")
else:
    print("Valor inválido")
