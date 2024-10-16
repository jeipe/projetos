from datetime import date
from datetime import datetime
from math import floor
class Cliente:
    def __init__(self, nome, cpf, dataN, telefone, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.dataN = dataN
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    
    # def aniversario(self, dataN):

    def tel(self):
        print(f'Bem vindo {self.nome}')
        print(f'cpf: {self.cpf}')
        print(f'nascimento: {self.dataN}')
        print(f'telefone: {self.telefone}')
        print(f'email: {self.email}')
        print(f'endereço: {self.endereco}')

    def anv(self):
        
        Idade = (date.today() - self.dataN)

        result = floor(Idade.days / 365.25)
        print(f'idade do clinte: {result}') #aqui vc tava tentando retornar self.result, mas não faz sentido porque não tem result nos selfs.
        return result

