import math

def delta(a,b,c):
	return b**2 - 4 * a *c


def primeira_raiz(a,b,c):
	return (-b + math.sqrt(delta(a,b,c))) / (2*a)

def segunda_raiz(a,b,c):
	return (-b -math.sqrt(delta(a,b,c))) / (2*a)



if __name__ == '__main__':
	a = float(input("Qual o número que acompanha x^2?"))
	b = float(input("Qual o número que acompanha x?"))
	c = float(input("Qual o número inteiro?"))
	
	valor_delta = delta(a,b,c)

	if valor_delta < 0:
		print("Esta equação não possui raízes reais")

	else:
		raiz_1 = primeira_raiz(a,b,c)
		raiz_2 = segunda_raiz(a,b,c)

		if valor_delta > 0: #imprime as duas raizes em ordem crescente
			if segunda_raiz(a,b,c) > primeira_raiz(a,b,c):
				print("As raízes da equação são",raiz_1,"e",raiz_2)

			else:
				print("As raízes da equação são",raiz_2,"e",raiz_1)

		else:
			print("A raíz dupla desta equação é",primeira_raiz(a,b,c))

