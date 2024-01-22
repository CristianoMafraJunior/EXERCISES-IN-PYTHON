#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
celsius = float(input("Digite sua temperatura em celsius: "))
converter_fahrenheit = (celsius * 9/5) + 32
print(f'Sua temperatura em Fahrenheit é {converter_fahrenheit}')