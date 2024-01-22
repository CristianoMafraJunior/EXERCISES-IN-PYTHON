# Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# #Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math 

def calcular_latas_galoes(area):
    cobertura_por_litro = 6
    cobertura_por_lata = 18 * cobertura_por_litro
    cobertura_por_galao = 3.6 * cobertura_por_litro

    #Compras apenas com latas de 18 litros
    latas_necessarias = math.ceil(area / cobertura_por_lata)
    preco_latas = latas_necessarias * 80.00

    #Compras apenas com galões de 3.6 litros
    galoes_necessarios = math.ceil(area / cobertura_por_galao)
    preco_galoes = galoes_necessarios * 25.00

    #Misturar latas e galões minimizando o desperdício
    latas_para_misturar = int(area // cobertura_por_lata)
    galoes_para_misturar = math.ceil((area % cobertura_por_lata) / cobertura_por_galao)
    
    preco_mistura = (latas_para_misturar * 80.00) + (galoes_para_misturar * 25.00)
    
    return (latas_necessarias, preco_latas), (galoes_necessarios, preco_galoes), (latas_para_misturar, galoes_para_misturar, preco_mistura)

def programa_tinturaria():
    area_para_pintar = int(input("Informe sua area para pintar: "))

    resultado_latas, resultado_galoes, resultado_mistura = calcular_latas_galoes(area_para_pintar)

    #Resultados 
    print("\nResultado lata de 18 litros")
    print(f"Quantidade de latas necessarias {resultado_latas[0]}")
    print(f"Preço total R$ {resultado_latas[1]:.2f}")

    print("\nResultado galão de 3.6 litros")
    print(f"Quantidade de galões necessarios {resultado_galoes[0]}")
    print(f"Preço total R$ {resultado_galoes[1]:.2f}")

    print("\nResultado da mistura")
    print(f"Quantidade de latas necessarias {resultado_mistura[0]}")
    print(f"Quantidade de galões necessarios {resultado_mistura[1]}")
    print(f"Preço total: R$ {resultado_mistura[2]:.2f}")

programa_tinturaria()