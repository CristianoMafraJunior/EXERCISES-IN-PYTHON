#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

class Turno:
    def informar_turno():
        while True:
            turno = input("Informe seu turno: (M/V/N/S): ") 
            if turno == "M":
                print("Bom dia!")
            elif turno == "V":
                print("Boa tarde!")
            elif turno == "N":
                print("Boa Noite!")
            elif turno == "S":
                print("Sair!")
                break
            else:
                print("Opção invalida")
 
    informar_turno()