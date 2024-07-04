def fatorial(n):
    fat = 1

    if n > 0:
        while n != 0:
            fat = fat * n
            n = n - 1
    return fat


def binomio(n,k):
    binomial = fatorial(n) / (fatorial(k) * fatorial(n-k))
	
    print(int(binomial))

if __name__ == '__main__':
    n=int(input("Digite um número:"))
    k=int(input("Digite a classe:"))

    binomio(n,k)