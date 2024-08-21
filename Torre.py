
from Aeroporto import Aeroporto

class Torre():

    def __init__(self, nome, aeroporto, quantidade_pistas):
        self.nome = nome
        self.aeroporto = aeroporto
        self.quantidade_pistas = quantidade_pistas


    def quantidade_pistas(numero):
        try:
            pistas = []
            for valores in range(numero):
                pistas.append(valores)
            return pistas
        except TypeError:
            print('Só é permitidos números')
        finally:
            print('Só é aceito números')

    def acessar_pistas(acesso):
        acesso = self.quantidade_pistas
        if len(acesso) == 0:
            print('Não a pistas liberadas')
        else:
            print('Existe uma quantidade de pistas disponíveis: ' + acesso)

    def liberacao_pistas(self):
        quantidade = self.quantidade_pistas
        return('Quantidade de pistas informadas: ' + quantidade)

    def permissao(self):
        pass
    
    def permissao_negada(self):
        pass


#juntar com aeroporto, pq é uma funcionalidade do aeroporto

#para o metodo liberação de pista, transformar a quantidade em uma lista de pistas, para o avião decolar ou pousar
