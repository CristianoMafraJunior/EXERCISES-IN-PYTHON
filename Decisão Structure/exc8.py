#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
#sabendo que a decisão é sempre pelo mais barato.
produtos = []
for i in range (1,4):
    produto = float(input(f"Informe o preço do produto {i}: "))
    produtos.append(produto)

menor_preco = min(produtos)
print(f"Menor Preço: R$ {menor_preco}")
