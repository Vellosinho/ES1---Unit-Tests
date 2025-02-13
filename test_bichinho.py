import unittest
import bichinho
import comida
import brinquedo

class TesteBichinho(unittest.TestCase):
    print('Testes da classe Bichinho')

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


if __name__ == '__main__':
    unittest.main()
