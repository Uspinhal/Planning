import pandas
import os


def menuInicial() -> int:
    UserInterface().mainInterface()
    opcao = int(input(">> "))
    return opcao


class UserInterface:
    """
    Classe de Interface com o usuário
    """
    
    def __init__(self, user: str = 'ADM'):
        self.user = user
    
    def mainInterface(self) -> None:
        """
        Tela inicial
        :return: None
        """
        os.system('cls')
        print('=====================================')
        print('============== Planning =============')
        print('=============== INÍCIO ==============')
        print('=====================================')
        print(f'Bem vindo: {self.user} \n')
        print('Selecione uma opção no menu: ')
        print('1 - Criar conta')
        print('2 - Efetuar lançamento')
        print('3 - Consultar saldo')
        print('0 - Sair do sistema')
    
    def criarContaGUI(self) -> None:
        # TODO: Criar GUI para criar conta
        pass
    
    def lancamentoGUI(self) -> None:
        """
        Tela de lançamentos
        :return: None
        """
        # TODO: Criar GUI para os lançamentos
        os.system('cls')
        print('=====================================')
        print('============== Planning =============')
        print('============= Lançamentos ===========')
        print('=====================================')
        print()
        print(f'Bem vindo: {self.user}')
    
    def saldoGUI(self, df: pandas.DataFrame) -> None:
        """
        Tela de Saldo
        :param df: pandas.DataFrame
        :return: None
        """
        os.system('cls')
        print('=====================================')
        print('============== Planning =============')
        print('=============== SALDO ===============')
        print('=====================================')
        print()
        print(f'Usuário: {self.user}')
        print('Escolha a conta para consultar o saldo: ')
        print(df[['Conta', 'Nome']])
