Aplicacao bichinho virtual - Lucas Gabriel Velloso 
RA: 790771

Funcionamento:

- Para testes automatizados: executar o comando:
    
    "python test_bichinho.py"

    Comando executa 12 testes automatizados:
    - Teste de criacao do bichinho Virtual
    - Teste de alimentacao
    - Teste de limpeza
    - Teste de diversao
    - Teste de toggle de descanso
    - Testes relacionados a passagem do tempo

- Para execucao do programa em si, executar o comando:

    "python main.py"

Como funciona o programa:

- ao se executar o arquivo main, o programa pede pra que voce insira um nome.
- Em seguida, o terminal era esperar um comando, que pode ser: "Comida, Banho, Brincar, Luz ou Sair"
- Caso o usuario insira o comando "Brincar", ele ira aumentar a diversao do bichinho em 50
- Caso escolha o comando "Banho", ira aumentar a higiene do bichinho em 100
- Caso escolha "Comida", ira alimentar o bichinho em 25
- Caso escolha "Luz", ira acender ou apagar a luz:

    - Caso a luz esteja apgada, o bichinho ira descansar a cada comando que o usuario insira
    - Caso contrario, ele so perdera todos os atributos normalmente

- Caso escolha "Sair", o terminal ira fechar
