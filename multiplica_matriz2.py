#https://www.beecrowd.com.br/repository/UOJ_2385.html

dimensão = int(input())

P, Q, R, S, X, Y = [int(x) for x in input().split()]

A = [[0]*dimensão for k in range(dimensão)]
B = [[0]*dimensão for k in range(dimensão)]

for i in range(1, dimensão+1):
    for j in range(1, dimensão+1):
        elemento_A = (P*i + Q*j) % X
        elemento_B = (R*i + S*j) % Y
        
        A[i-1][j-1] = elemento_A
        B[i-1][j-1] = elemento_B

i_C, j_C = [int(x) for x in input().split()]

elemento_C = 0

for m in range(dimensão):
    elemento_C += A[i_C-1][m] * B[m][j_C-1]
        
print(elemento_C)