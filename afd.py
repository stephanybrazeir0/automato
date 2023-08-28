with open("alfabeto.txt","r") as file:
    conteudo = file.read()
    linhas = conteudo.split("\n")

alfabeto = linhas[1].split(" ")
estadoInicial = linhas[0]
estadosFinais = linhas[3].split(" ")
estados = linhas[2].split(" ")
transicoes = linhas[4:]

def executaAutomato():
    while True:
        palavra = input("Digite a palavra: ")
        
        if palavra.lower() == 'sair':
            print("Encerrando...")
            break  
        
        estadoAtual = estadoInicial
        
        def buscaEstados(estado, letra):
            for transicao in transicoes:
                t = transicao.split(" ")
                if t[0] == estado and t[2] == letra:
                    return t[1]
            return None
        
        print(estadoAtual+"\n-para o estado")
        i = -1
        for caractere in palavra:
            i += 1
            estadoAtual = buscaEstados(estadoAtual, caractere)
            if estadoAtual is None:
                print("Rejeita\n")
                break
            if i != len(palavra) - 1:
                print(estadoAtual+", consumindo um '"+caractere+"'")
                print("-para o estado")
            else:
                print(estadoAtual+", consumindo um '"+caractere+"'")
                if estadoAtual in estadosFinais:
                    print("Aceita\n")
                else:
                    print("O estado "+estadoAtual+" não é um estado Final, portando a palavra é rejeitada\n")

        resposta = input("Deseja inserir outra palavra? (sim/nao): ")
        if resposta.lower() != 'sim':
            print("Encerrando...")
            break  

executaAutomato()
