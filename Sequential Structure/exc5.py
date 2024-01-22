# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
Fahrenheit = int(input("Informe sua Temperatura em Fahrenheit: "))
converter_Celsius = 5 *((Fahrenheit - 32) / 9)

print(f'Sua temperatura em Celsius é {converter_Celsius:.0f}')