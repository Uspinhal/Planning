# import datetime
import pandas as pd
from time import sleep

from dao.historico import Historico
from gui.userInterface import UserInterface
from planning.dao.conta import Conta


def main() -> None:
    """
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
    """
    c = menuInicial()
    while c != 0:
        if c == 1:
            print('1 - Criar conta')
            sleep(2)
            c = menuInicial()
        elif c == 2:
            print('2 - Efetuar lançamento')
            sleep(2)
            c = menuInicial()
        elif c == 3:
            print('3 - Consultar saldo')
            menuSaldo()
            sleep(2)
            c = menuInicial()

    print('Saindo...')
    sleep(2)
    

def menuInicial() -> int:
    ui = UserInterface()
    ui.mainInterface()
    opcao = int(input(">> "))
    return opcao


def menuSaldo() -> None:
    df = pd.read_csv('database/contas.csv')
    ui = UserInterface()
    ui.saldoGUI(df)
    c = int(input('>>'))
    conta = Conta(c)
    print(f'Seu saldo é: {conta.saldo}')
    

def movimentacao(arquivo: str, conta: Conta, data: str, desc: str, valor: float, mov: str) -> None:
    movements = Historico(arquivo, conta.numero, data, desc, valor, mov)
    movements.movimento()
    conta.atualizaSaldo(valor, mov)
    

def aux() -> None:
    conta: Conta = Conta(numero=1)
    # conta.criaConta()
    # print('done')
    print(conta.existeConta(1))
    

if __name__ == '__main__':
    operacao = True
    if operacao:
        main()
    else:
        aux()
