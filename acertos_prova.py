def teste():
    respostas = 'abcbdab'
    gabarito = 'aecbaab'
    print(acertos(respostas,gabarito))

def acertos(resposta, gabarito):
    acertos = 0
    for i in range(len(gabarito)):
        if resposta[i] == gabarito[i]:
            acertos += 1

    return acertos
            
            
if __name__== '__main__' :
    respostas = input("Digite as respostas: ")
    gabarito = input("Digite o gabarito: ")

    print(acertos(respostas,gabarito))
