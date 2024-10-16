from datetime import date
from datetime import datetime
from cliente import Cliente
import datetime
class Transacao:
    def __init__(self, valor, data, tipo, origem, hora):
        self.valor = valor
        self.data = data
        self.tipo = tipo
        self.origem = origem
        self.hora = hora

    
    def transacao(self):
        print('------Transação------')
        print(f'valor: {self.valor}')
        print(f'data: {date.today()}')
        print(f'tipo: {self.tipo}')
        print(f'origem: {self.origem}')
        print(f'hora: {self.hora}')