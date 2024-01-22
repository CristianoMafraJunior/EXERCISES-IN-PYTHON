# Faça um Programa que peça 2 números inteiros e um número real(Float). Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num1_int = int(input("Digite seu numero: "))
num2_int = int(input("Digite seu numero: "))
num_real = float(input("Digite seu numero: "))

resultado1 = (num1_int * 2) *  (num2_int / 2 )
resultado2 = (num1_int * 3) + num_real
resultado3 = num_real ** 3


print(resultado1)
print(resultado2)
print(resultado3)