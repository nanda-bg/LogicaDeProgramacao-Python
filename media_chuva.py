matriz = []
media = []
for i in range(12):
    matriz.append([int(x) for x in input().split()])

media.append(sum(matriz[0])/31)
media.append(sum(matriz[1])/28)

for i in range(2, 7):
    if i % 2 == 0:
        divisor = 31
    else:
        divisor = 30

    media.append(sum(matriz[i])/divisor)

for i in range(7, 12):
    if i % 2 == 0:
        divisor = 30
    else:
        divisor = 31

    media.append(sum(matriz[i])/divisor)


for j in range(len(media)-1):
    print(f"{media[j]:.2f}", end=' ')

print(f"{media[-1]:.2f}")

