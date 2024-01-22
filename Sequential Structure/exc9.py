# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
sexo = input("Informe seu sexo: (M/F): ")

peso_ideal_mas = (72.7* altura) - 58
peso_ideal_fem = (62.1* altura) - 44.7

if sexo == 'F':
     print(f'Seu peso ideal é KG {peso_ideal_fem:.2f}')
elif sexo == 'M':
     print(f'Seu peso ideal é KG {peso_ideal_mas:.2f}') 
else:
    print("Opção Invalida")