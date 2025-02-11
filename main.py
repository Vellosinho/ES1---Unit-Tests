# Execucao do programa:

# Cria a instancia do bichinho
from bichinho import BichinhoVirtual


nomeDoBichinho = input("Nome do bichinho: ")
novoBichinho = BichinhoVirtual(nomeDoBichinho)
comando = input("Comida, Banho, Brincar ou Luz: ")
print()


# Permanece excutando em loop ate que o usuario escolha sair
while (comando != "Sair"):
    novoBichinho.passaTimer()
    
    match comando:
        case "Comida":
            novoBichinho.alimentaBichinho(25)
            print("Voce alimentou o " + novoBichinho.nomeBichinho)
        case "Banho":
            novoBichinho.limpaBichinho(100)
            print("Agora "+ novoBichinho.nomeBichinho + " esta limpinho")
        case "Brincar":
            novoBichinho.brincaBichinho(50)
            print("Voce brincou com " + novoBichinho.nomeBichinho)
        case "Luz":
            novoBichinho.toggleBichinhoDescansando()
            if (novoBichinho.bichinhoDescansando):
                print("Voce apagou a luz, agora " + novoBichinho.nomeBichinho + " esta descansando")
            else:
                print("Voce acendou a luz, " + novoBichinho.nomeBichinho + " esta pronto pra ficar com voce")
        case _:
            print("Comando invalido")

    
    # Retorna o estado atual do bichinho
    print("Bichinho: "+ novoBichinho.nomeBichinho)
    print("Fome: "+ str(novoBichinho.alimentacaoBichinho))
    print("Higiene: "+ str(novoBichinho.higieneBichinho))
    print("Diversao: "+ str(novoBichinho.diversaoBichinho))
    print("Energia: "+ str(novoBichinho.energiaBichinho))
    
    # Pega o proximo comando:
    comando = input("Comida, Banho, Bricar ou Luz: ")
    print()