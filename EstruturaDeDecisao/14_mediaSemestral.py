# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento	Conceito
# Entre 9.0 e 10.0	A
# Entre 7.5 e 9.0	B
# Entre 6.0 e 7.5	C
# Entre 4.0 e 6.0	D
# Entre 4.0 e zero	E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

n1 = float(input("Informe a 1º nota: "))
n2 = float(input("Informe a 2º nota: "))

media = (n1 + n2) / 2
conceito = ''
situacao = ""

if media <= 10.0 and media > 9:
    conceito = 'A'
    situacao = "Aprovado"
elif media <= 9.0 and media > 7.5:
    conceito = 'B'
    situacao = "Aprovado"
elif media <= 7.5 and media > 6.0:
    conceito = 'C'
    situacao = "Aprovado"
elif media <= 6.0 and media > 4.0:
    conceito = 'D'
    situacao = "Reprovado"
elif media <= 4.0 and media > 0:
    conceito = 'E'
    situacao = "Reprovado"
    
    
print(f'1º nota: {n1}\n2º nota {n2}\nMédia: {media}\nConceito: {conceito}\n{situacao}')