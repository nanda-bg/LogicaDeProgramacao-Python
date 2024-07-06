#https://www.beecrowd.com.br/repository/UOJ_1181.html

linha = int(input())
operação = input()

matriz = [[0]*12 for i in range(12)]

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

soma = 0

for k in range(12):
    soma += matriz[linha][k]

if operação == 'S':
    print(soma)

else:
    print(f'{soma/12:.1f}')