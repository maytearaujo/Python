# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input("Informe o tamanho de um arquivo para download (em MB): "))
velocidade = float(input("Informe a velocidade de um link de Internet (em Mbps): "))

velocidade = velocidade / 8
tempoDownload = tamanho / velocidade
tempoDownload = tempoDownload / 100

print("O tempo aproximado de download do arquivo é: " +str(tempoDownload) +" minutos")