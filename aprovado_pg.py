nota1 = input()
nota2 = input()
nota3 = input()
nota4 = input()

notas = [nota1, nota2, nota3, nota4]

valor_notas = {'A': 4, 'B': 3, 'C': 2, 'D': 0}

aprovado = True

for i in notas:
    if valor_notas[i] < 2:
        aprovado = False
        break

print(aprovado)