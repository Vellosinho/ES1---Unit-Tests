import unittest
import bichinho
import comida


class TesteComida(unittest.TestCase):
    print('Testes da classe Comida')
    
    #Testes relacionados as comidas:
        # testa criacao de comidas do tipo fruta:
    def test_cria_fruta(self):
        comidaTeste = comida.Comida('Morango', 'Fruta')
        self.assertEqual(comidaTeste.valorNutricional, 25)


    # testa criacao de comidas do tipo racao:
    def test_cria_racao(self):
        comidaTeste = comida.Comida('Pedigree', 'Racao')
        self.assertEqual(comidaTeste.valorNutricional, 50)


    # testa criacao de comidas de outros tipos
    def test_cria_outro(self):
        comidaTeste = comida.Comida('Lasanha', 'Massa')
        self.assertEqual(comidaTeste.valorNutricional, 10)


    # testa preparo de frutas:
    def test_prepara_fruta(self):
        comidaTeste = comida.Comida('Morango', 'Fruta')
        comidaTeste2 = comida.Comida('Abacaxi', 'Fruta')
        comidaTeste3 = comida.Comida('Laranja', 'Fruta')
        comidaTeste.preparaFruta(comidaTeste2, comidaTeste3)

        self.assertEqual(comidaTeste.nomeComida, 'Salada de frutas')
        self.assertEqual(comidaTeste.valorNutricional, 75)


    # testa preparo de frutas errado:
    def test_prepara_fruta_errada(self):
        comidaTeste = comida.Comida('Pedigree', 'Racao')
        comidaTeste2 = comida.Comida('Abacaxi', 'Fruta')
        comidaTeste3 = comida.Comida('Laranja', 'Fruta')
        comidaTeste.preparaFruta(comidaTeste2, comidaTeste3)
        
        self.assertNotEqual(comidaTeste.nomeComida, 'Salada de frutas')
        self.assertNotEqual(comidaTeste.valorNutricional, 75)


    
    # teste relacionado a fusao de ambas as classes:
    def test_alimenta_fruta_pro_bichinho(self):
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')
        comidaTeste = comida.Comida('Morango', 'Fruta')

        bichinhoTeste.alimentaComidaBichinho(comidaTeste)

        self.assertEqual(bichinhoTeste.alimentacaoBichinho, 25) 


    # teste de alimentacao de racao para o bichinho
    def test_alimenta_racao_pro_bichinho(self):
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')
        comidaTeste = comida.Comida('Pedigree', 'Racao')

        bichinhoTeste.alimentaComidaBichinho(comidaTeste)

        self.assertEqual(bichinhoTeste.alimentacaoBichinho, 50) 


    # teste de alimentacao de racao para o bichinho
    def test_alimenta_outro_pro_bichinho(self):
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')
        comidaTeste = comida.Comida('Macarrao', 'Massa')

        bichinhoTeste.alimentaComidaBichinho(comidaTeste)

        self.assertEqual(bichinhoTeste.alimentacaoBichinho, 10) 

    # Testes relacionados a classe Brinquedo:

        

if __name__ == '__main__':
    unittest.main()