import pandas as pd
from csv import DictWriter, DictReader


class Conta:
    def __init__(self, numero: int = 0, nome: str = "", banco: str = "", saldo: float = 0.0):
        self.__file = 'database/contas.csv'
        if self.existeConta(numero):
            self.__numero = numero
            self.__nome = self._carregaConta().loc[self._carregaConta()["Conta"] == self.numero, "Nome"]
            self.__banco = self._carregaConta().loc[self._carregaConta()["Conta"] == self.numero, "Banco"]
            self.__saldo = self._carregaConta().loc[self._carregaConta()["Conta"] == self.numero, "Saldo"]
        else:
            self.__numero = numero
            self.__nome = nome
            self.__banco = banco
            self.__saldo = 0.0
        
    @property
    def numero(self):
        return self.__numero
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def banco(self):
        return self.__banco
    
    @property
    def saldo(self):
        return self.__saldo
    
    @classmethod
    def _carregaConta(cls) -> pd.DataFrame:
        df = pd.read_csv('database/contas.csv')
        return df
    
    def existeConta(self, numero: int) -> bool:
        """
        Retorna True se existe uma conta e False se não existe
        :param numero: int
        :return: bool
        """
        df = self._carregaConta()
        selecao = df.loc[df['Conta'] == numero]
        if selecao.empty:
            return False
        else:
            return True
        
    def debito(self, valor) -> float:
        self.__saldo -= valor
        return self.__saldo
    
    def credito(self, valor) -> float:
        self.__saldo += valor
        return self.__saldo
       
    def criaConta(self) -> None:
        """
        Cria a conta no sistema
        :return: None
        """
        df = self._carregaConta()
        self.__numero = df["Conta"].max() + 1
        with open(self.__file, 'a', newline='') as arquivo:
            cabecalho = ['Conta', 'Banco', 'Nome', 'Saldo']
            escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
            escritor_csv.writerow({"Conta": self.numero, "Banco": self.banco, "Nome": self.nome, "Saldo": self.saldo})
    
    def atualizaSaldo(self, valor: float, operacao: str) -> None:
        """
        Atualiza saldo da conta
        :param valor: float
        :param operacao: str
        :return: None
        """
        if operacao == 'saque':
            saldo = self.debito(valor)
            # print(f'Operação: {operacao}, Saldo: {saldo}')
        elif operacao == 'deposito':
            saldo = self.credito(valor)
            # print(f'Operação: {operacao}, Saldo: {saldo}')
        else:
            saldo = self.__saldo
        
        df = self._carregaConta()
        df.loc[df["Conta"] == self.numero, "Saldo"] = saldo
        df.to_csv(self.__file, index=False)
        print(df.head())
     
    def procuraConta(self, numero: int) -> dict:
        pass
