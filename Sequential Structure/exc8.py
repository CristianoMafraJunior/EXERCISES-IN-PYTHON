# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

peso_ideal = (72.7* altura) - 58

print(f'Seu peso ideal é KG {peso_ideal}')