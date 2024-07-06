#https://www.beecrowd.com.br/repository/UOJ_1187.html

operação = input()

matriz = [[0]*12 for i in range(12)]

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

for j in range(12): #elementos na dp e acima viram 0
    for i in range (j, 12):
        matriz[i][j] = 0

for j in range(11, -1, -1): # elementos na ds e abaixo viram 0
    for i in range(11-j, 12):
        matriz[i][j] = 0

soma = 0

for k in range(len(matriz)):
    soma += sum(matriz[k])

if operação == 'S':
    print(soma)

else:
    print(f'{soma/30:.1f}')