# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

horas = float(input("Quantas Horas você trabalhou no mês: "))
ganho_por_hora = float(input("Quantos você ganha por hora: "))

salario = (horas * ganho_por_hora)
imposto = salario * 0.10
salario_limpo = salario - imposto

print(f'Seu salario sujo é R$ {salario:.2f}')
print(f'Seu salario limpo é R$ {salario_limpo:.2f}')
