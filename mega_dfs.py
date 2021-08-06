# Alunos: Adrio Oliveira Alves (nUSP:11796830), Eduardo Vinicius Barbosa Rossi (nUSP:10716887)


from ler_pajek import *
from math import inf
from enum import Enum


class Cor(Enum):
    B = 1
    C = 2
    P = 3


#Classe grafo
class Grafo:
    def __init__(self, n_vertices, m_adj, valores, direcionado=False):
        #Inicalizam-se variáveis
        self.n = n_vertices
        self.dir = direcionado
        self.val = True if valores != None else False
        
        #Listas das cores dos vértices são inicializadas
        self.cinzas = []
        self.pretas = []
        self.brancas = []

        self.vertices = []
        for i in range(len(m_adj)):
            self.vertices.append(
                Vertice(m_adj[i], i, valores[i] if self.val is True else False))

    def __repr__(self):
        string = ''
        for i in range(len(self.vertices)):
            string += str(i)+': '
            string += str(self.vertices[i])
            string += '\n'
        return string


#Classe vértice
class Vertice:
    def __init__(self, adjacencias, id, valores):
        #Inicializam-se variáveis
        self.id = id
        self.adj = adjacencias

        self.valores_adj = valores

        self.visitado = False
        self.raiz = False
        self.pai = None
        self.tempo_c = inf
        self.tempo_p = inf
        self.cor = Cor.B

    def __repr__(self):
        lista = [x+1 for x in self.adj]
        return str(lista)



def DFS(grafo, v, pais):
    # O algoritmo para obter os pais dos sorvedouros funcionará da seguinte forma: adicionamos o pai obtido quando se chega em um
    #vértice sorvedouro na lista de pais, o outro pai será adicinado à lista quando atigirmos um vértice preto com a DFS
    v.cor = Cor.C

    for i in v.adj:
        #Vértice pintado de preto significa que pode ser um sorvedouro

        if grafo.vertices[i].cor == Cor.P:
            #Caso o descendente atual for de cor Preta significa que ambos os pais desse vértice são descendentes do vértice inicial
            if len(grafo.vertices[i].adj) == 0:
                #Vértice pintado de preto sem filhos significa que é sorvedouro, então adiciona o pai na lista de pais
                pais[ i ].append( v.id )
        
        #Se a cor do vértice for branco chama a função novamente
        elif grafo.vertices[i].cor == Cor.B:
            filho = DFS(grafo, grafo.vertices[i], pais)
            #Obtém o filho sorvedouro com o retorno da função

            #Se retornou None, é porque o filho não é sorvedouro
            if filho != None:
                #Guarda v na lista de pais de sorvedouros
                pais[filho].append( v.id )

    v.cor = Cor.P

    #Se o vértice atual for sorvedouro, ou seja, sem filhos, retorna seu valor
    if len (v.adj) == 0:
        return v.id
    else:
        return None


#BFS padrão
def BFS (grafo, n, start_v):
    d=[]
    preto = list()
    cinza = list()
    branco = list()

    for i in range(n):
        d.append(inf)
        branco.append(i)
    
    cinza.append(start_v.id)
    d[start_v.id] = 0
    branco.remove(start_v.id)

    while len(cinza) != 0:
        v = cinza.pop(0)
        preto.append(v)
        for w in grafo.vertices[v].adj:
            if w in branco:
                d[w] = d[v] + 1
                cinza.append(w)
                branco.remove(w)

    return d


def main():
    nome_arquivo = input()
    vertices, valores = lerPajek(nome_arquivo)
    g = Grafo(len(vertices), vertices, valores)
    #Fim da inicialização

    #Matriz de pais de sorvedouros inicializada
    pais = [ [] for i in range(len(vertices)) ]

    distancia_minima = inf
    sorvedouros_minimos = []

    #Obtém os sorvedouros e seus pais a partir da DFS
    DFS(g, g.vertices[0], pais)

    #Obtém a lista de distancias do vértice inicial
    d = BFS(g, len(g.vertices), g.vertices[0])

    #Percorrendo a lista de sorvedouros
    for i in range(len(pais)):
        #O sorvedouro deve ter dois pais descendentes do vértice inicial
        if len(pais[i]) == 2:
            #Calcula a soma das distancias dos pais do vértice sorvedouro i (d[X]+d[Y])
            soma_distancias_pais = d[ pais[i][0] ] + d[ pais[i][1] ]

            #Caso a distancia minima for maior que a soma dos pais atuais
            if soma_distancias_pais < distancia_minima:
                #Muda o valor da distancia minima
                distancia_minima = soma_distancias_pais
                #Apaga os sorvedouros_minimos antigos, pois suas distancias agora são maiores que o valor minimo
                sorvedouros_minimos.clear()
                #Adiciona o novo sorvedouro_minimo
                sorvedouros_minimos.append( i+1 )

            #Caso a distancia minima for igual a soma dos pais atuais
            elif soma_distancias_pais == distancia_minima:
                #Adiciona o sorvedouro atual a lista de sorvedouros_minimos
                sorvedouros_minimos.append( i+1 )

    print( '\n'.join(str(i) for i in sorvedouros_minimos) )
                
    return


if __name__ == '__main__':
    main()