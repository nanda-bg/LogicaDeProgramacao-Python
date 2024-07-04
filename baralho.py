#https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/baralho/

import re

def quantas_cartas(cartas):
    baralho = re.findall("...", cartas) #separa as cartas, cada uma com 3 caracteres
    copas = []
    espadas = []
    ouros = []
    paus = []

    for i in range(len(baralho)): #agrupa as cartas de acordo com o naipe
        carta = baralho[i]
        match carta[-1]: #verifica o naipe
            case "C":
                copas.append(carta)
            case "E":
                espadas.append(carta)
            case "U":
                ouros.append(carta)
            case "P":
                paus.append(carta)
              

    return copas, espadas, ouros, paus

def repetidas(lista_naipe):
    conjunto = set(lista_naipe)
    
    if len(conjunto) != len(lista_naipe): #verifica se tem cartas repetidas
        return 'erro'
    


def teste():
    cartas = "01C02C03C04C05C07C09C10C11C02E02E03E11U" # input()
    baralho = quantas_cartas(cartas)

    for i in range(len(baralho)):
        if repetidas(baralho[i]) == "erro":
            print("erro")
        elif len(baralho[i]) == 13: #baralho completo
            print(0);
        else:
            print(13 - len(baralho[i])) #quantas cartas faltam
                  
        
if __name__== "__main__":
    teste()