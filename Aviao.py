from Torre import Torre
from Aeroporto import Aeroporto

class  Aviao:

    def __init__(self, potencia, modelo, quantidade_passageiros, quant_bagagem, comunic_torre):
        self.potencia = potencia
        self.modelo = modelo
        self.quantidade_passageiros = quantidade_passageiros
        self.quant_bagagem = quant_bagagem
        self.comunic_torre = comunic_torre

    
    def aceleracao(self):
        pass

    def aterrissagem(self):
        pass

    def pneu(self):
       pneu = pneu.settar() 
       return False


    def verificacao_pneus(self):
        status_pneu = self.pneu()
        if status_pneu == False and self.aceleracao == True:
            return ('Permitido decolar, aguardando liberação da torre')
        else:
            print('Existe algo de errado, por favor, verificar com a torre')

    def comandos_torre(self):
        if Torre.permissao  == True:
            print('Autorizada decolagem')
            return self.aceleracao
        elif Torre.permissao_negada == True:
            print('Manter a posição')


#fazer verificação de erro caso execeder a quantidade de bagagem e passageiros, contanto com a tripulação