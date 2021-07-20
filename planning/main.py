# import datetime
import pandas as pd
from time import sleep

from dao.historico import Historico
from gui.userInterface import UserInterface
from planning.dao.conta import Conta
from planning.gui.userInterface import menuInicial
from planning.utils.utils import formata_float_str_moeda as fmt


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
            # TODO: Inserir método para criar conta
            print('1 - Criar conta')
            sleep(2)
            c = menuInicial()
        elif c == 2:
            # TODO: Inserir método para fazer os lançamentos
            print('2 - Efetuar lançamento')
            gui.lancamentoGUI()
            sleep(2)
            c = menuInicial()
        elif c == 3:
            menuSaldo()
            c = menuInicial()

    print('Saindo...')
    sleep(2)
    

def menuSaldo() -> None:
    df = pd.read_csv('database/contas.csv')
    gui.saldoGUI(df)
    c = int(input('>>'))
    conta = Conta(c)
    print(f'Seu saldo é: {fmt(conta.saldo)}')
    espera = input("Pressione qualquer tecla para continuar...")
    

def movimentacao(arquivo: str, conta: Conta, data: str, desc: str, valor: float, mov: str) -> None:
    movements = Historico(arquivo, conta.numero, data, desc, valor, mov)
    movements.registro()
    conta.atualizaSaldo(valor, mov)
    

def aux() -> None:
    conta: Conta = Conta(numero=1)
    # conta.criaConta()
    # print('done')
    print(conta.existeConta(1))
    

if __name__ == '__main__':
    gui = UserInterface(user='ADM')
    operacao = True
    if operacao:
        main()
    else:
        aux()
