"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) 
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220
"""
class CalculoFolhaDePagamento:
    def __init__(self):
        self.horas = 0
        self.valor_horas = 0.0
        self.salario = 0.0
        self.desconto_ir = 0

    def calculo_folha(self):
        self.horas = int(input("Informe suas horas: "))
        self.valor_horas = float(input("Informe quanto custa sua hora: "))

        self.salario = self.horas * self.valor_horas

        if self.salario <= 900:
            self.desconto_ir = 0
        elif 900 < self.salario <= 1500:
            self.desconto_ir = 0.05 * self.salario
        elif 1500 < self.salario <= 2500:
            self.desconto_ir = 0.10 * self.salario
        elif self.salario > 2500:
            self.desconto_ir = 0.20 * self.salario
        
        desconto_sindicato = 0.03 * self.salario

        fgts = 0.11 * self.salario

        salario_liquido = self.salario - self.desconto_ir - desconto_sindicato

        self.imprimir_folha(self.desconto_ir, desconto_sindicato, salario_liquido, fgts)

    def imprimir_folha(self, desconto_ir, desconto_sindicato, salario_liquido, fgts):
        print(f"Salário Bruto: R$ {self.salario:.2f}")
        print(f"Desconto IR: R$ {desconto_ir:.2f}")
        print(f"Desconto Sindicato: R$ {desconto_sindicato:.2f}")
        print(f"FGTS: R$ {fgts:.2f}")
        print(f"Salário Líquido: R$ {salario_liquido:.2f}")

folha_pagamento = CalculoFolhaDePagamento()
folha_pagamento.calculo_folha()
