def binario(num):
    binario = ''
    
    while num // 2 > 0:
        binario += str(num % 2)
        num = num // 2

    binario += str(num) #adiciona 0 ou 1 ao final
    binario = binario[::-1] #inverte a ordem dos números

    return binario

if __name__ == '__main__':
    for i in range(5):
        num_natural = int(input("Digite um número natural: "))
        print(binario(num_natural))
