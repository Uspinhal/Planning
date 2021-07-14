class UserInterface:
    def __init__(self):
        pass
    
    def mainInterface(self) -> int:
        print('=====================================')
        print('============== Planning==============')
        print('============== GUI ==================')
        print('=====================================')
        
        print('Selecione uma opção no menu: ')
        print('1 - Criar conta')
        print('2 - Efetuar saque')
        print('3 - Efetuar depósito')
        print('4 - Efetuar transferência')
        print('5 - Listar contas')
        print('6 - Sair do sistema')
        
        opcao: int = int(input())
        
        return opcao
