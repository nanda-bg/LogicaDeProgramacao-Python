#https://www.beecrowd.com.br/repository/UOJ_2293.html

linhas, colunas = [int(x) for x in input().split()]

campo = []

for i in range(linhas):
    campo.append([int(x) for x in input().split()])

total_minhocas = 0

for j in range(colunas):
    soma_coluna = 0
    for i in range(linhas):
        soma_coluna += campo[i][j]
    
    if soma_coluna > total_minhocas:
        total_minhocas = soma_coluna
    
    if sum(campo[i]) > total_minhocas:
        total_minhocas = sum(campo[i])

print(total_minhocas)