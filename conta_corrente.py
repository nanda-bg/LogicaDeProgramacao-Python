class conta_corrente:
    def __init__(self, conta, nome , saldo=0):
        self.conta = int(conta) #número da conta
        self.nome = nome
        self.saldo = float(saldo)

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        
    def deposito(self, deposito):
        self.saldo += deposito 
        
    def saque(self, saque):
        if saque > self.saldo:
            print('Saldo insuficiente')
        else:
            self.saldo -= saque
        