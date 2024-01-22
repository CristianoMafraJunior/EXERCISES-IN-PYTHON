#Faça um programa para a leitura de duas notas parciais de um aluno. 
#O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

notas = []
for i in range(1,3):
    nota = float(input(f'Informe sua nota {i}: '))
    notas.append(nota)

media = sum(notas) / len(notas)
if media == 10.0:
    print("Aprovado com Distinção")
elif media >= 7.0:
    print("Aprovado")
elif media < 7.0:
    print("Reprovado")


