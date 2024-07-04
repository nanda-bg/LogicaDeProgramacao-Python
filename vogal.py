def vogal(letra):
    vogais = ['a', 'e', 'i', 'o', 'u']

    if letra in vogais:
        return True
    
    else:
        return False

	
letra =input("Digite uma letra:")
vogal(letra)

