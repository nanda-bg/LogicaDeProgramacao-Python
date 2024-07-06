while True:
    try:
        tamanho = int(input())
    
        matriz = [[0]*tamanho for i in range(tamanho)]
    
        for i in range(tamanho):
            for j in range(tamanho):
                if i == j:
                    matriz[i][j] = 2
    
                elif i + j == tamanho-1:
                    matriz[i][j] = 3
    
        uns = (tamanho // 3)
    
        for i in range(uns, tamanho-uns):
            for j in range(uns, tamanho-uns):
                matriz[i][j] = 1
    
        meio = tamanho//2
    
        matriz[meio][meio] = 4
    
        for i in range(tamanho):
            for j in range(tamanho-1):
                print(matriz[i][j], end= '')
            print(matriz[i][-1])
        
        print()
            
    except EOFError:
        break