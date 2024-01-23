"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
class AumentoSalario:
    def __init__(self):
        self.salario = 0.0

    def aumentar_salario(self):
        self.salario = float(input("Informe salario: R$ "))

        percentual = 0.0  # Inicializa o percentual com 0
        if self.salario <= 280:
            percentual = 0.20
        elif 280 < self.salario <= 700:
            percentual = 0.15
        elif 700 < self.salario <= 1500:
            percentual = 0.10
        else:
            percentual = 0.05

        aumento = self.salario * percentual
        novo_salario = self.salario + aumento

        return novo_salario, percentual, aumento  

    def imprimir_salario(self):
        novo_salario, percentual, aumento = self.aumentar_salario()
        print(f"Salario antes do reajuste: R$ {self.salario:.2f}")
        print(f"Percentual aplicado: {percentual * 100:.2f}%")
        print(f"Valor do aumento: R$ {aumento:.2f}")
        print(f"Novo salário: R$ {novo_salario:.2f}")


aumento = AumentoSalario()

aumento.imprimir_salario()


