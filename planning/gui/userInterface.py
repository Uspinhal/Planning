import pandas


class UserInterface:
    def __init__(self, user: str = 'ADM'):
        self.user = user
    
    def mainInterface(self) -> None:
        print('=====================================')
        print('============== Planning==============')
        print('============== GUI ==================')
        print('=====================================')
        print()
        print(f'Bem vindo: {self.user}')
        
        print('Selecione uma opção no menu: ')
        print('1 - Criar conta')
        print('2 - Efetuar lançamento')
        print('3 - Consultar saldo')
        print('0 - Sair do sistema')
    
    def criarContaGUI(self) -> None:
        pass
    
    def lancamentoGUI(self) -> None:
        pass
    
    def saldoGUI(self, df: pandas.DataFrame) -> None:
        print('=====================================')
        print('============== Planning==============')
        print('============== GUI ==================')
        print('=====================================')
        print()
        print(f'Usuário: {self.user}')
        print('Escolha a conta para consultar o saldo: ')
        print(df[['Conta', 'Nome']])
