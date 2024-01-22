# Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
#e que a tinta é vendida em latas de 18 litros, 
#que custam R$ 80,00. Informe ao usuario a quantidades de latas de tinta a seram compradas e o preço total

import math 

def calcular_latas(area):
    cobertura_por_lata = 18 * 3
    quantidade_lata = math.ceil(area / cobertura_por_lata)
    return quantidade_lata

def preco_por_lata(quantidade_lata):
    preco_lata = 80.00
    preco_total = preco_lata * quantidade_lata
    return preco_total

def solicitar_area():
    area_para_pintar = int(input("Informe a aerea que você deseja pintar: "))

    latas_necessarias = calcular_latas(area_para_pintar)

    preco_total = preco_por_lata(latas_necessarias)

    print(f"Quantidade de latas necessarias: {latas_necessarias}")
    print(f"Preço total R$ {preco_total}")

solicitar_area()