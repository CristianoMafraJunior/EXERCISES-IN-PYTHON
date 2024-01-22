#Faça um Programa que peça dois números e imprima o maior deles.

nm1 = int(input("informe seu numero: "))
nm2 = int(input("informe seu numero: "))

if nm1 > nm2:
    print(f"{nm1} é maior")
elif nm1 < nm2:
    print(f"{nm2} é maior")
else:
    print("Numeros são iguais")