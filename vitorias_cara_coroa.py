# 0 = Maria
# 1 = Joao

partidas = int(input())
while partidas > 0:
    ganhou = input().split()

    vitorias_joão = 0
    vitorias_maria = 0

    for i in range (partidas):
        if ganhou[i] == '0':
            vitorias_maria += 1
        else:
            vitorias_joão += 1

    print(f'Mary won {vitorias_maria} times and John won {vitorias_joão} times')

    partidas = int(input())
