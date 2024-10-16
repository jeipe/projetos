from transacao import Transacao
from conta_banco import Banco
from cliente import Cliente
from datetime import date
from datetime import datetime
import datetime
cliente1 = Cliente('joão', '69444141', date(2007,8,14), '548154687', 'joao@gmail.com', 'rua b casa a ')
cliente1.tel()
cliente1.anv()
# quando for colocar data usa 'date(ano,mes,dia)'

conta = Banco(50, 501, 9804, 500.000)
conta.exi()

Transacao1 = Transacao(10, 'pix', 'joao', '19:56', '210')
Transacao1.transacao()

agora = datetime.datetime.now()
