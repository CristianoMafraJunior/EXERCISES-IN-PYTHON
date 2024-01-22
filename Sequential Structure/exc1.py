#CTRL K + CTRL C COMENTA O CODIGO SELECIONADO
#Append vai adicionando na lista
notas = []

for i in range (1,11):
        nota = float(input(f'Digite sua notas {i}: '))
        notas.append(nota)

media = sum(notas) / len(notas)

print(f'Sua media é {media:.2f}')