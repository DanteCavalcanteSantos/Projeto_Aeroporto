
from Aeroporto import Aeroporto

class Torre():

    def __init__(self, nome, aeroporto, quantidade_pistas):
        self.nome = nome
        self.aeroporto = aeroporto
        self.quantidade_pistas = quantidade_pistas


    def liberacao_pistas(self):
        quantidade = self.quantidade_pistas
        return('Quantidade de pistas informadas: ' + quantidade)

    def permissao(self):
        pass
    
    def permissao_negada(self):
        pass
