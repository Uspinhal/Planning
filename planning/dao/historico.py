# import datetime
# from csv import writer
from csv import DictWriter


class Historico:
    def __init__(self, file: str, conta: int, data: str, desc: str, valor: float, movimentacao: str):
        """
        Inicializador da classe DataBase
        """
        self.__file = file
        self.__data = data
        self.__desc = desc
        self.__valor = valor
        self.__movimentacao = movimentacao
        self.__conta = conta
    
    @property
    def data(self) -> str:
        return self.__data
    
    @property
    def desc(self) -> str:
        return self.__desc
    
    @property
    def valor(self) -> float:
        return self.__valor
    
    @property
    def movimentacao(self) -> str:
        return self.__movimentacao

    def registro(self) -> None:
        """
        Faz o registros das operações
        :return: None
        """
        with open(self.__file, 'a', newline='') as arquivo:
            cabecalho = ['Data', 'Histórico', 'Valor', 'Conta', 'Operação']
            escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
            escritor_csv.writerow({"Data": self.data, "Histórico": self.desc, "Valor": self.valor,
                                   "Conta": self.__conta, "Operação": self.movimentacao})
        


        print(f'Data: {self.data} | Histórico: {self.desc} | Valor: R${self.valor}')


"""
    def criaArquivo(self, path, file):
        with open(path+file+".csv", 'w',newline='') as arquivo:
            cabecalho = ['Data', 'Histórico', 'Valor']
            escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
            escritor_csv.writeheader()
"""
