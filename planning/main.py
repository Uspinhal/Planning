# import datetime
from dao.historico import Historico
from planning.dao.conta import Conta


def main() -> None:
    # data = input('Data: ')
    # desc = input('Descrição: ')
    # valor = input('Valor: ')
    conta: Conta = Conta(numero=1, nome='Neon', banco='Neon')
    arquivo = 'database/historico.csv'
    data = '13/07/2021'
    desc = 'testando mais uma vez'
    valor = 50
    mov = 'saque'
    movimentacao(arquivo, conta, data, desc, valor, mov)
    

def movimentacao(arquivo: str, conta: Conta, data: str, desc: str, valor: float, mov: str) -> None:
    movements = Historico(arquivo, conta.numero, data, desc, valor, mov)
    movements.movimento()
    conta.atualizaSaldo(valor, mov)
    

def aux() -> None:
    conta: Conta = Conta(nome='Itau', banco='Itau', saldo=0.0)
    conta.criaConta()
    print('done')


if __name__ == '__main__':
    operacao = True
    if operacao:
        main()
    else:
        aux()
