class Brinquedo:
    nomeBrinquedo = ''
    diversaoBrinquedo = 0
    durabilidadeBrinquedo = 0
    brinquedoQuebrado = False
    
    def __init__(self, nome, diversao, durabilidade, quebrado):
        self.nomeBrinquedo = nome
        self.diversaoBrinquedo = diversao
        self.durabilidadeBrinquedo = durabilidade
        self.brinquedoQuebrado = quebrado

    
    def reduzDurabilidade(self):
        self.durabilidadeBrinquedo = self.durabilidadeBrinquedo - 1
        if (self.durabilidadeBrinquedo == 0):
            self.quebraBrinquedo()

    def quebraBrinquedo(self):
        self.diversaoBrinquedo = 0
        self.brinquedoQuebrado = True