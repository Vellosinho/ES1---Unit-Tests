# O codigo abaixo propoe o funcionamento de um bichinho virtual.

# A classe definida abaixo e a classe do proprio bichinho, que e criada com os atributos alimentacao, higiene, diversao, e energia, alem de uma booleana que controla se o bichinho esta ou nao descansandn

import brinquedo
class BichinhoVirtual:
    nomeBichinho = ''
    alimentacaoBichinho = 0
    higieneBichinho = 0
    diversaoBichinho = 0
    energiaBichinho = 0
    bichinhoDescansando = False
    brinquedoBichinho = brinquedo.Brinquedo('Nenhum', 0, 0, True)

    def __init__(self, nome):
        self.nomeBichinho = nome

    def alimentaBichinho(self, x):
        # essa funcao alimenta o bichinho, ou seja, recebe um valor x que vai ser somado a fome do bichinho. Quando a fome vale zero, o bichinho esta com muita fome e deve ser alimentado

        # se a alimentacao do bichinho atingir o teto (100), o numero deve parar de crescer:
        self.alimentacaoBichinho += x
        if (self.alimentacaoBichinho > 100):
            self.alimentacaoBichinho = 100

        return self
    
    def alimentaComidaBichinho(self, comida):
        self.alimentaBichinho(comida.valorNutricional)

    def daBrinquedoBichinho(self, brinquedo):
        self.brinquedoBichinho = brinquedo
    
    def limpaBichinho(self, x):
        # essa funcao limpa o bichinho, ou seja, recebe um valor x que vai ser somado a higiene. Quando a higiene vale zero, o bichinho esta muito sujo e deve ser limpado

        # O mesmo vale para as demais funcoes:
        self.higieneBichinho += x
        if (self.higieneBichinho > 100):
            self.higieneBichinho = 100

        return self
    
    def brincaBichinho(self, x):
        # essa funcao diverte o bichinho, ou seja, soma um valor (x) a diversao dele. Quando esse valor for 0, o bichinho esta entediado e deve ser entretido
        self.diversaoBichinho += x

        if (self.diversaoBichinho > 100):
            self.diversaoBichinho = 100
        
        return self
    
    def toggleBichinhoDescansando(self):
        # essa funcao controla o status do bichinho, ou seja, se ele esta ou nao descansando. se esta descansando, ao passar do tempo a energia do bichinho sera resposta, caso contrario, ela sera removida
        self.bichinhoDescansando = not self.bichinhoDescansando

        return self

    def passaTimer(self):
        # essa funcao e implementada dentro de um timer que a dispara periodicamente. ela checa se o bichinho esta descansando ou nao, para controlar a atualizacao da energia, e fora isso, so subtrai os valores dos outros contadores do bichinho

        # Da mesma forma que o limite dos atributos eh 100, o limite da falta deles eh 0:
        if (not self.bichinhoDescansando) :
            self.energiaBichinho -= 5
            if (self.energiaBichinho < 0):
                self.energiaBichinho = 0
        else :
            self.energiaBichinho += 10
            if (self.energiaBichinho > 100):
                self.energiaBichinho = 100
        self.alimentacaoBichinho -= 5
        if (self.alimentacaoBichinho < 0):
            self.alimentacaoBichinho = 0
        self.higieneBichinho -= 5
        if (self.higieneBichinho < 0):
            self.higieneBichinho = 0
        if (self.brinquedoBichinho.brinquedoQuebrado == True) :
            self.diversaoBichinho -= 5
            if (self.diversaoBichinho < 0):
                self.diversaoBichinho = 0
        else:
            self.brincaBichinho(self.brinquedoBichinho.diversaoBrinquedo)
            self.brinquedoBichinho.reduzDurabilidade()

        return self
    
    def retornaEstado(self):

        return self
    
