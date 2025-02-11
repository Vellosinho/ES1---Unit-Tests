# O codigo abaixo propoe o funcionamento de um bichinho virtual.

# A classe definida abaixo e a classe do proprio bichinho, que e criada com os atributos alimentacao, higiene, diversao, e energia, alem de uma booleana que controla se o bichinho esta ou nao descansandn
class Comida:
    nomeComida = ''
    tipo = ''
    valorNutricional = 0


    def __init__(self, nome, tipo):
        self.nomeComida = nome
        self.tipo = tipo
        self.defineValorNutricional()


    def defineValorNutricional(self):
        if (self.tipo == 'Fruta'):
            self.valorNutricional = 25
        elif (self.tipo == 'Racao'):
            self.valorNutricional = 50
        else:
            self.valorNutricional = 10
        
        return
    
    def preparaFruta(self, fruta, fruta2):
        if (self.tipo == 'Fruta'):
            self.nomeComida = 'Salada de frutas'
            self.valorNutricional += fruta.valorNutricional + fruta2.valorNutricional

        return
