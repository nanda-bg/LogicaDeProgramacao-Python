#https://www.beecrowd.com.br/repository/UOJ_1184.html

operação = input()

matriz = [[0]*12 for i in range(12)]

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())


soma = 0
divisor = 0

for j in range(11):
    for i in range (j+1, 12):
        soma += matriz[i][j]
        divisor += 1

if operação == 'S':
    print(soma)

else:
    print(f'{soma/divisor:.1f}')