#Faça um Programa que leia três números e mostre-os em ordem decrescente

numeros = []
for i in range(1,4):
    numero = int(input("Informe seu numero: "))
    numeros.append(numero)

numeros_ordenados = sorted(numeros, reverse=True)
print(f"Números ordenados de ordem descresente: {numeros_ordenados}")

