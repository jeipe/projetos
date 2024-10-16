class Banco:
    def __init__(self, num_age, num_cont, tipo, saldo):
        self.num_age = num_age
        self.num_cont = num_cont
        self.tipo = tipo
        self.saldo = saldo
    
    def exi(self):
        print('-----conta-----')
        print(f'numero da agencia: {self.num_age}')
        print(f'numero da conta: {self.num_cont}')
        print(f'tipo da conta: {self.tipo}')
        print(f'saldo: {self.saldo}')
