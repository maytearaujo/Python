# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salarioHora = float(input("Informe o valor da hora trabalhada: "))
horasTrabalhadas = float(input("Informe a quantidades de horas trabalhadas no mês: "))

salarioMensal = salarioHora * horasTrabalhadas
print("O Salário mensal é: R$ " + str(salarioMensal))