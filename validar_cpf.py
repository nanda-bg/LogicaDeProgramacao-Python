def validar(cpf):
    cpf = cpf.replace('.','')
    cpf = cpf.replace('-', '')

    conjunto = set(list(cpf))
    if len(conjunto) > 1:
        multiplicador = len(cpf)-1
        parada = multiplicador-1
        comparador = -2
        valido = True

        while comparador < 0 and valido:
            i = 0
            soma = 0
            while i < parada:
                soma += int(cpf[i]) * multiplicador
                multiplicador -= 1
                i += 1
                
            resto = soma%11

            if  (resto <= 9 and int(cpf[comparador]) == 11-resto) or (resto > 9 and int(cpf[comparador]) == 0):
                    multiplicador = len(cpf)
                    parada = multiplicador-1
                    comparador += 1
            else:
                valido = False
    
    else:
         valido = False

    return valido

def teste():
    print(validar('105.425.439-74')) #True
    print(validar('81815434244')) #True
    print(validar('2154200')) #False
    print(validar('11111111111')) #False
    print(validar('818.154.342-44')) #True
    print(validar('22222222222')) #False (os números não podem ser todos iguais)

if __name__ == '__main__':
    teste()
    
