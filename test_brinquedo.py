import unittest
import bichinho
import brinquedo


class TesteBrinquedo(unittest.TestCase):
    print('Testes da classe Brinquedo')

    # Testes relacionados a classe Brinquedo:

    # teste de criacao do brinquedo:
    def test_cria_brinquedo(self):
        brinquedoTeste = brinquedo.Brinquedo('Bolinha', 10, 5, False)
        
        self.assertEqual(brinquedoTeste.nomeBrinquedo, 'Bolinha')
        self.assertEqual(brinquedoTeste.diversaoBrinquedo, 10)
        self.assertEqual(brinquedoTeste.durabilidadeBrinquedo, 5)
    

    # teste reducao da durabilidade do Brinquedo
    def test_reduz_durabilidade_brinquedo(self):
        brinquedoTeste = brinquedo.Brinquedo('Bolinha', 10, 5, False)

        brinquedoTeste.reduzDurabilidade()
        self.assertEqual(brinquedoTeste.durabilidadeBrinquedo, 4)


    # teste de dar brinquedo pro bichinho:
    def test_da_brinquedo_pro_bichinho(self):
        brinquedoTeste = brinquedo.Brinquedo('Bolinha', 10, 5, False)
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')

        bichinhoTeste.daBrinquedoBichinho(brinquedoTeste)

        self.assertEqual(bichinhoTeste.brinquedoBichinho.nomeBrinquedo, 'Bolinha')


    # teste bichinho com brinquedo passagem timer:   
    def test_brinquedo_com_passa_timer(self):
        brinquedoTeste = brinquedo.Brinquedo('Bolinha', 10, 5, False)
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')

        bichinhoTeste.daBrinquedoBichinho(brinquedoTeste)

        bichinhoTeste.passaTimer()

        self.assertEqual(bichinhoTeste.diversaoBichinho, brinquedoTeste.diversaoBrinquedo)


    # teste bichinho com brinquedo passagem timer:   
    def test_quebra_brinquedo(self):
        brinquedoTeste = brinquedo.Brinquedo('Bolinha', 10, 1, False)
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')

        bichinhoTeste.daBrinquedoBichinho(brinquedoTeste)
        bichinhoTeste.passaTimer()

        self.assertEqual(bichinhoTeste.brinquedoBichinho.brinquedoQuebrado, True)


    # teste bichinho com brinquedo passagem timer:   
    def test_quebra_brinquedo_com_timer(self):
        brinquedoTeste = brinquedo.Brinquedo('Bolinha', 10, 1, False)
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')

        bichinhoTeste.daBrinquedoBichinho(brinquedoTeste)
        bichinhoTeste.passaTimer()
        bichinhoTeste.passaTimer()

        self.assertEqual(bichinhoTeste.diversaoBichinho, 5)

        

if __name__ == '__main__':
    unittest.main()