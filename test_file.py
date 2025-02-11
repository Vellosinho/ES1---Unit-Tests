import unittest
import bichinho
import comida

class TesteBichinho(unittest.TestCase):

    # Teste criacao do bichinho
    def test_cria_bichinho(self):
        #  Cria o bichinho com um nome e confere se o nome e o que foi passado.
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')
        self.assertEqual(bichinhoTeste.nomeBichinho, 'Pedro')


    # teste de alimentacao do bichinho:
    def test_alimenta_bichinho(self):
        # Cria o bichinho, o alimenta e verifica se a alimentacao dele corresponde com o valor que foi passado:
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')
        bichinhoTeste.alimentaBichinho(15)
        self.assertEqual(bichinhoTeste.alimentacaoBichinho, 15)


    # teste de limpeza do bichinho:
    def test_limpa_bichinho(self):
        # Cria o bichinho, o limpa e verifica se a higiene dele corresponde com o valor que foi passado:
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')
        bichinhoTeste.limpaBichinho(10)
        self.assertEqual(bichinhoTeste.higieneBichinho, 10)


    # teste de diversao do bichinho:
    def test_brinca_bichinho(self):
        # Cria o bichinho, o limpa e verifica se a higiene dele corresponde com o valor que foi passado:
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')
        bichinhoTeste.brincaBichinho(20)
        self.assertEqual(bichinhoTeste.diversaoBichinho, 20)


    # teste de colocar o bichinho pra descansar:
    def test_descansa_bichinho(self):
        #Cria o bichinho e o coloca pra descansar, verificando se a variavel de controle do descanso e retornada verdadeira
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')
        bichinhoTeste.toggleBichinhoDescansando()
        self.assertTrue(bichinhoTeste.bichinhoDescansando)


    # teste de realimentacao do bichinho:
    def test_alimenta_bichinho_novamente(self):
        # Cria o bichinho, o alimenta duas vezes e verifica se o valor vale o mesmo que a soma das duas alimentacoes
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')
        bichinhoTeste.alimentaBichinho(15)
        bichinhoTeste.alimentaBichinho(15)
        self.assertEqual(bichinhoTeste.alimentacaoBichinho, 30)


    # primeiro teste de ativacao das funcoes do timer:
    def test_passa_timer(self):
        # Cria o bichinho, o alimenta e verifica se e o coloca para descansar. Entao verifica se a fome diminnui e a energia sobe
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')
        bichinhoTeste.alimentaBichinho(30)
        bichinhoTeste.toggleBichinhoDescansando()
        bichinhoTeste.passaTimer()

        # Checa se os valores correspondem ao resultado esperado
        self.assertEqual(bichinhoTeste.alimentacaoBichinho, 25)
        self.assertEqual(bichinhoTeste.higieneBichinho, 0)
        self.assertEqual(bichinhoTeste.diversaoBichinho, 0)
        self.assertEqual(bichinhoTeste.energiaBichinho, 10)


    # teste limites alimentacao, higiene e diversao:
    def test_limites(self):
        # Testa o limite da alimentacao, higiene e 
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')
        bichinhoTeste.alimentaBichinho(150)
        bichinhoTeste.brincaBichinho(150)
        bichinhoTeste.limpaBichinho(150)

        # Assegura-se que a alimentacao nao ultrapassou o limite: 
        self.assertEqual(bichinhoTeste.alimentacaoBichinho, 100)
        # Assegura-se que a higiene nao ultrapassou o limite:
        self.assertEqual(bichinhoTeste.higieneBichinho, 100)
        # Assegura-se que a diversao nao ultrapassou o limite:
        self.assertEqual(bichinhoTeste.diversaoBichinho, 100)


    def test_limite_descanso_bichinho(self):
        # Inicializa o bichinho
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')
        bichinhoTeste.toggleBichinhoDescansando()

        # Faz o bichinho descansar 11 vezes, o que daria um resultado de 110:
        bichinhoTeste.passaTimer()
        bichinhoTeste.passaTimer()
        bichinhoTeste.passaTimer()
        bichinhoTeste.passaTimer()
        bichinhoTeste.passaTimer()
        bichinhoTeste.passaTimer()
        bichinhoTeste.passaTimer()
        bichinhoTeste.passaTimer()
        bichinhoTeste.passaTimer()
        bichinhoTeste.passaTimer()
        bichinhoTeste.passaTimer()
        self.assertEqual(bichinhoTeste.energiaBichinho, 100)

    
    # Testa a alimentacao do bichinho como se comporta na aplicacao:
    def test_alimentacao_aplicacao(self):
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')
        bichinhoTeste.alimentaBichinho(25)
        bichinhoTeste.passaTimer()
        bichinhoTeste.alimentaBichinho(25)
        self.assertEqual(bichinhoTeste.alimentacaoBichinho, 45)


    # Testa a limpeza do bichinho como se comporta na aplicacao:
    def test_limpa_bichinho_aplicacao(self):
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')
        bichinhoTeste.passaTimer()
        bichinhoTeste.limpaBichinho(100)
        self.assertEqual(bichinhoTeste.higieneBichinho, 100)


    # Testa a limpeza do bichinho como se comporta na aplicacao:
    def test_brinca_bichinho_aplicacao(self):
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')
        bichinhoTeste.brincaBichinho(50)
        bichinhoTeste.passaTimer()
        self.assertEqual(bichinhoTeste.diversaoBichinho, 45)

    
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

        bichinhoTeste.alimentaBichinho(comidaTeste.valorNutricional)

        self.assertEqual(bichinhoTeste.alimentacaoBichinho, 25) 


    # teste de alimentacao de racao para o bichinho
    def test_alimenta_racao_pro_bichinho(self):
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')
        comidaTeste = comida.Comida('Pedigree', 'Racao')

        bichinhoTeste.alimentaBichinho(comidaTeste.valorNutricional)

        self.assertEqual(bichinhoTeste.alimentacaoBichinho, 50) 


    # teste de alimentacao de racao para o bichinho
    def test_alimenta_outro_pro_bichinho(self):
        bichinhoTeste = bichinho.BichinhoVirtual('Pedro')
        comidaTeste = comida.Comida('Macarrao', 'Massa')

        bichinhoTeste.alimentaBichinho(comidaTeste.valorNutricional)

        self.assertEqual(bichinhoTeste.alimentacaoBichinho, 10) 


if __name__ == '__main__':
    unittest.main()