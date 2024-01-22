#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Informe sua letra: ")
vogal = "aeiou"

def verificar_vogal():
    if letra.lower() in vogal:
        print('É vogal')
    else:
        print("É consoante")

verificar_vogal()

#Função lower usada para comparação