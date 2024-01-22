ganho_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhada = int(input("Quantas horas você trabalho no mês? "))

salario_bruto = ganho_hora * horas_trabalhada
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindicato

print(f"Salário Bruto: R$ {salario_bruto}")
print(f"Desconto INSS: R$ {desconto_inss}")
print(f"Desconto IR: R$ {desconto_ir}")
print(f"Desconto Sindicato: R$ {desconto_sindicato}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")

