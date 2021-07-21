# import datetime
import pandas as pd
from time import sleep

from dao.historico import Historico
from gui.userInterface import UserInterface
from planning.dao.conta import Conta
from planning.utils.utils import formata_float_str_moeda as fmt

# TODO: Fazer o tratamento de erro


def main() -> None:
    c = menuInicial()
    
    while c != 0:
        if c == 1:
            # TODO: Inserir método para criar conta
            print('1 - Criar conta')
            sleep(2)
            c = menuInicial()
        elif c == 2:
            menuLancamento()
            c = menuInicial()
        elif c == 3:
            menuSaldo()
            c = menuInicial()

    print('Saindo...')
    sleep(2)
    

def menuInicial() -> int:
    gui.mainInterface()
    opcao = int(input(">> "))
    return opcao


def menuLancamento() -> None:
    gui.lancamentoGUI()
    op = input('>> ')
    if op == "1":
        op = 'saque'
    else:
        op = 'deposito'
    nr_conta = int(input('Entre com o número da Conta:'))
    data = input('Entre com a data: ')
    desc = input('Entre com a descrição: ')
    valor = input('Entre com o valor: ')
    value = float(valor)
    conta = Conta(nr_conta)
    conta.atualizaSaldo(value, op)
    Historico(conta.numero, data, desc, value, op).registro()


def menuSaldo() -> None:
    df = pd.read_csv('database/contas.csv')
    gui.saldoGUI(df)
    c = int(input('>>'))
    conta = Conta(c)
    print(f'Seu saldo é: {fmt(conta.saldo)}')
    input("Pressione qualquer tecla para continuar...")
    

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
