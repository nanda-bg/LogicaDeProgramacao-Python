def incomodam(n, vezes=""):
    if n>0:
        vezes= "incomodam "+ incomodam(n-1,vezes)
        
    return vezes


def elefantes(n, musica="Um elefante incomoda muita gente\n",x=2):
    if x<=n :
        musica = musica + str(x) + " elefantes "+ str(incomodam(x)) + "muito mais\n"
        if n-1>=x:
            musica=musica + str(x) + " elefantes incomodam muita gente\n"
            x+=1
            musica=elefantes(n,musica,x)
        return musica

    elif n<2:
        return ""
        

def teste():
    print(elefantes(4))

    print(elefantes(7))

if __name__ == "__main__":
    teste()
