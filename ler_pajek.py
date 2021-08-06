#Lê o arquivo pajek


def lerPajek(nome_arquivo):

    n = 0
    arquivo = open(nome_arquivo)

    #Ler n° de vertices (n)
    linha1 = arquivo.readline()

    if '*Vertices' in linha1.split()[0]:
        n = int(linha1.split()[1])

        #Cria as listas
        vertices = [list() for _ in range(n)]
        #Cria a lista de valores para usar no grafo valorado
        valores = [list() for _ in range(n)]

        #Ler a segunda linha
        linha2 = arquivo.readline()

        #Confere qual é o formato do grafo
        if '*Edges' in linha2:
            #Se estiver escrito '*Edges' o grafo é não dirigido
            dir = False
        elif '*Arcs' in linha2:
            #Se estiver escrito '*Arcs' o grafo é dirigido
            dir = True

    #Lê cada linha
    for linha in arquivo.readlines():
        if len(linha) <= 1:
            continue

        linha = linha.split()

        #Adiciona a aresta lida na lista
        vertices[int(linha[0])-1].append(int(linha[1])-1)

        #Se o grafo for não dirigido adiciona a aresta que 'volta' também
        if dir == False:
            vertices[int(linha[1])-1].append(int(linha[0])-1)

        #Se o grafo for valorado escreve os valores na matriz de valores
        if len(linha) == 3:
            valores[int(linha[0])-1].append(int(linha[2]))
            if dir == False:
                valores[int(linha[1])-1].append(int(linha[2]))

    arquivo.close()

    if len(valores[0]) == 0:
        valores = None

    return vertices, valores
