def somas_iguais(matriz):
    soma = sum(matriz[0])

    soma_dp = 0
    soma_ds = 0

    for i in range(len(matriz)):
        if sum(matriz[i]) != soma:
            return False
        
        soma_coluna = 0
        for j in range(len(matriz)):
            soma_coluna += matriz[j][i]

            if i == j:
                soma_dp += matriz[i][j]

            if i+j == len(matriz)-1:
                soma_ds += matriz[i][j]

        if soma_coluna != soma:
            return False
        
    if soma_dp != soma or soma_ds != soma:
        return False
    
    
    return True


    
dimensão = int(input())

matriz = []

for i in range(dimensão):
    matriz.append([int(x) for x in input().split()])

print(somas_iguais(matriz))