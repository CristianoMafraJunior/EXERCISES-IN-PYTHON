# Faça um programa que peça o tamanho de um arquivo para download (em MB) 
# e a velocidade de um link de Internet (em Mbps), calcule e 
# informe o tempo aproximado de download do arquivo usando este link (em minutos).
def calcular_minutos():
    tamanho_mb = float(input("Digite tamanho do arquivo em MB: "))
    velocidade_mbps = float(input("Digite a velocidade da sua internet: "))

    tempo_download_minutos = (tamanho_mb / (velocidade_mbps / 8)) / 60

    print(f"Tempo para dowland do arquivo em minutos é {tempo_download_minutos} minutos")

calcular_minutos()