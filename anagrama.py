palavra_1 = input()
palavra_2 = input()

if palavra_1 != palavra_2:
    print( sorted(list(palavra_1)) == sorted(list(palavra_2)) )

else:
    print('False')