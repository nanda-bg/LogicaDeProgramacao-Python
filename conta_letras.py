def conta_letras(frase, contar= "vogais" ):
    frase=frase.replace(" ","")
   
    qnts_vogais = 0

    vogais=["a","e","i","o","u"]


    # while i < len(frase):
    #     j=0
    #     while j < len(vogais):
    #         if frase[i]==vogais[j]:
    #             quantidade+=1
    #         j+=1
    #     i+=1

    for letra in frase:
        if letra in vogais:
            qnts_vogais += 1

    if contar == "vogais":
        return qnts_vogais
    else:
        return len(frase)-qnts_vogais

def teste():
    frase='programamos em python'
    print(conta_letras(frase))

    frase='programamos em python'
    print(conta_letras(frase,'vogais'))

    frase='programamos em python'
    print(conta_letras(frase, 'consoantes'))

if __name__ == '__main__':
    teste()
