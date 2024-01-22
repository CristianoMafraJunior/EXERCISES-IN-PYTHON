#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Digite a letra (M/F): ")

if letra == 'M':
    print("Masculino")
elif letra == 'F':
    print("Feminino")
else:
    print("Sexo inválido")