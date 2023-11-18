# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

salarioHora = float(input("Informe o valor da hora trabalhada: "))
horasTrabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salarioBruto = salarioHora * horasTrabalhadas

ImpostoRenda = salarioBruto * 0.11
INSS = salarioBruto * 0.08
sindicato = salarioBruto * 0.05

salarioLiquido = salarioBruto - (ImpostoRenda + INSS + sindicato)

print(f'Salário Bruto: {round(salarioBruto)}\n Imposto de Renda: {round(ImpostoRenda)}\nINSS: {round(INSS)}\nSindicato: {round(sindicato)}\nSalário Liquido: {round(salarioLiquido)}')