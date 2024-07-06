#https://www.beecrowd.com.br/repository/UOJ_1557.html

ordem = int(input())

while ordem != 0:

    matriz = [[0]*ordem for i in range(ordem)]
    

    for i in range(ordem):
        for j in range(ordem):
            if j == 0 and i == 0:
                matriz[i][j] = 1
            elif j == 0:
                 matriz[i][j] = matriz[i-1][0] * 2
            else:
                matriz[i][j] = matriz[i][j-1] * 2

    comprimento = len(str(matriz[ordem-1][ordem-1]))

    for i in range(ordem):
        for j in range(ordem):
            if j == ordem-1:
                print(f'{matriz[i][j]:{comprimento}d}')
            else:
                print(f'{matriz[i][j]:{comprimento}d}', end= ' ')
    

    ordem = int(input())

    if ordem != 0:
        print()
