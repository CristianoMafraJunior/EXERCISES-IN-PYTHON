#Faça um Programa que leia três números e mostre o maior deles.

numeros = []
for i in range(1,4):
    numero = int(input(f"Digite seu numero {i}: "))
    numeros.append(numero)

maior_numero = max(numeros)

print(f"Maior numero é: {maior_numero}")
