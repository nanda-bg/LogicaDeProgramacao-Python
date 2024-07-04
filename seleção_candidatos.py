def aprovação (candidatos, regra, num_vagas, aprovados):
    regra = regra.split()

    ordem_categorias = regra[-1].split(';')

   
    for j in range (len(ordem_categorias)):
        categorias = ordem_categorias[j].split(',')
        i = 0
        
        while i < len(candidatos) and num_vagas > 0:
            candidato = candidatos[i].split()
            categorias_candidato = candidato[-1].split(',')
       
            for categoria in categorias_candidato:
                if categoria in categorias:
                    aprovados.append(candidato[1])
                    num_vagas -= 1
                    break
            i += 1

    return aprovados, num_vagas



if __name__ == '__main__':
    regras = []
    regra = input()
   
    while regra != '0 0':
        regras.append(regra)
        regra = input()
   
   
    regra_geral = regras[0].split()

    qnt_categorias = len(regra_geral[-1].split(','))
    num_vagas = dict()
   
    for i in range(qnt_categorias):
       vaga = input().split()
       num_vagas[vaga[0]] = int(vaga[1])
           
       
       
    num_candidatos = int(input())
    candidatos = []
   
    for i in range(num_candidatos):
        candidatos.append(input())
       
   
   
    aprovados = []
    for i in range(len(regras)):
        regra = regras[i]
        categoria = regra.split()[2]
        vagas = num_vagas[regra.split()[2]]
        
        aprovados, vagas_restantes = aprovação (candidatos, regra, vagas, aprovados)

        candidatos = [aluno for aluno in candidatos if aluno.split()[1] not in aprovados]

        num_vagas[categoria] = vagas_restantes


    chaves = list(num_vagas.keys())
    
    for chave in chaves:
        if num_vagas[chave] != 0:
            regra = '10 10 AC AC'
            vagas = num_vagas[chave]

            aprovados, vagas_restantes = aprovação (candidatos, regra, vagas, aprovados)
            candidatos = [aluno for aluno in candidatos if aluno.split()[1] not in aprovados]
            num_vagas[chave] = vagas_restantes
        
    aprovados = sorted(aprovados)
    for i in range(len(aprovados)):
        print(aprovados[i])
    




# Exemplo entrada:
        
# 1 1 AC AC,LI_EP,LI_PCD,LI_Q,LI_PPI,LB_EP,LB_PCD,LB_Q,LB_PPI
# 2 1 LI_EP LI_EP
# 2 2 LI_PCD LI_PCD
# 2 3 LI_Q LI_Q
# 2 4 LI_PPI LI_PPI
# 2 5 LB_EP LB_EP
# 2 6 LB_PCD LB_PCD
# 2 7 LB_Q LB_Q
# 2 8 LB_PPI LB_PPI
# 3 1 LI_EP LI_PCD,LI_Q,LI_PPI;LB_PCD,LB_Q,LB_PPI;LB_EP
# 3 2 LI_PCD LI_Q,LI_PPI;LB_PCD;LB_Q,LB_PPI;LI_EP;LB_EP
# 3 3 LI_Q LI_PCD,LI_PPI;LB_Q;LB_PCD,LB_PPI;LI_EP;LB_EP
# 3 4 LI_PPI LI_PCD,LI_Q;LB_PPI;LB_PCD,LB_Q;LI_EP;LB_EP
# 3 5 LB_EP LB_PCD,LB_Q,LB_PPI;LI_PCD,LI_Q,LI_PPI;LI_EP
# 3 6 LB_PCD LB_Q,LB_PPI;LI_PCD;LI_Q,LI_PPI;LB_EP;LI_EP
# 3 7 LB_Q LB_PCD,LB_PPI;LI_Q;LI_PCD,LI_PPI;LB_EP;LI_EP
# 3 8 LB_PPI LB_PCD,LB_Q;LI_PPI;LI_PCD,LI_Q;LB_EP;LI_EP
# 4 1 LI_EP AC
# 4 2 LI_PCD AC
# 4 3 LI_Q AC
# 4 4 LI_PPI AC
# 4 5 LB_EP AC
# 4 6 LB_PCD AC
# 4 7 LB_Q AC
# 4 8 LB_PPI AC
# 0 0
# AC 15
# LI_EP 3
# LI_PCD 1
# LI_Q 1
# LI_PPI 2
# LB_EP 3
# LB_PCD 1
# LB_Q 1
# LB_PPI 3
# 40
# 1 88920 AC
# 2 21196 AC
# 3 41406 AC
# 4 76595 AC
# 5 21458 AC
# 6 54856 LB_EP,LB_PPI
# 7 26690 AC
# 8 33485 AC
# 9 96009 AC
# 10 15733 LI_EP
# 11 99148 AC
# 12 31918 LB_EP
# 13 21848 AC
# 14 87848 LI_EP,LI_PPI
# 15 39946 AC
# 16 22533 LI_EP
# 17 71231 AC
# 18 33920 LI_EP,LI_Q
# 19 98515 AC
# 20 84651 AC
# 21 25656 LI_EP
# 22 78816 AC
# 23 91312 AC
# 24 99072 LB_EP
# 25 43047 LI_EP,LI_Q,LB_PPI
# 26 38148 LB_EP,LB_PCD,LB_Q
# 27 66822 AC
# 28 90719 LI_EP
# 29 35645 AC
# 30 56119 LB_EP
# 31 93775 AC
# 32 64698 LB_EP,LB_PCD
# 33 80656 LI_EP
# 34 99512 AC
# 35 55262 LB_EP,LB_PPI
# 36 38248 LI_EP,LI_PPI
# 37 92869 LB_Q
# 38 20008 AC
# 39 89338 LI_EP,LI_PPI
# 40 81763 AC


#Saída esperada:
# 15733
# 21196
# 21458
# 21848
# 22533
# 25656
# 26690
# 31918
# 33485
# 33920
# 38148
# 38248
# 39946
# 41406
# 43047
# 54856
# 55262
# 56119
# 64698
# 71231
# 76595
# 80656
# 87848
# 88920
# 89338
# 90719
# 92869
# 96009
# 99072
# 99148