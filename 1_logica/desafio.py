
# -*- coding: utf-8 -*-

"""
@author: Lucas Hernandes da Costa Porto 
@email: lucashnds@usp.br
"""


def criaGrafo(vertices):
    """
    Cria um grafo vazio em um dicionario em que as chaves sao os vertices
    Entrada:
        vertices (int) -> Numero de vertices do grafo, que vao ser as chaves
    Saida:
        (dict) -> {'vertice 1':[], 'vertice 2':[], ..., 'vertice n':[]}
    """
    grafo = {}
    
    # cria uma lista de 1 a numero de vertices
    for v in range(1, vertices+1):
        grafo[v] = []
        
    return grafo
    
    
def preencheGrafo(grafo, arestas):
    """
    Faz um loop em uma range(arestas) e le entradas A e B e
    adicina no objeto grafo[A] a respectiva conexao B, e, sendo uma relacao reciproca:
    grafo[B] a respectiva conexao A
    
    Entrada:
        grafo (dict) -> {'vertice 1':[], 'vertice 2':[], ..., 'vertice n':[]} criado em criaGrafo()
        arestas (int) -> Numero de arestas a adicionar
    Saida:
        (dict) -> {'vertice 1':[conexao 1, conexao 2, ..., conexao n], ..., 
                   'vertice n':[conexao 1, conexao 2, ..., conexao n]}
    """
    
    for con in range(arestas):
        A, B = [int(i) for i in input().split()]
        grafo[A].append(B)
        grafo[B].append(A)
    
    return grafo


def countGrupos(grafo):
    """
    Contagem de micro grupos no grafo fazendo um loop por cada membro e 
    verificando na sua lista de amizades se possui algum vinculo com o membro anterior 
    no loop ou com alguns dos gruposa anteriores ja visitados, caso possua nao faz nada
    pois ainda é considerado um grupo de conexoes, caso o contrario incrementa a contagem de 
    grupos, caso seja uma lsita vazia incrementa a contagem tambem pois é considerado como
    um micro grupo
    
    Entrada:
        grafo (dict) -> {'vertice 1':[conexao 1, conexao 2, ..., conexao n], ..., 
                         'vertice n':[conexao 1, conexao 2, ..., conexao n]}
                        criado em preencheGrafo()
    Saida:
        (int) -> Numero de grupos
    """

    ligacoes = []
    lista_auxiliar = [] # A lista auxiliar vai guardar todos os grupos que ja foram visitados
    
    # cria uma lista de lista com os membros se suas conexoes
    # tipo: [[vertice 1, conexao 1, conexao 2, ..., conexao n] ...]
    # assim o vertice (membro) é incluso na verificação de conexoes
    for i, item in enumerate(grafo):
        ligacoes.append(grafo[item])
        ligacoes[i].append(item)
    
    grupos = 0
    
    for i, ligacao in enumerate(ligacoes):
        
        # No caso de membros isolados incrementa a variavel como um microgrupo
        if ligacao == []:
            grupos += 1
        
        else:
            # como é o primeiro indice nao compra com anterior e ja incrementa grupos
            if i == 0: 
                grupos += 1
            else:
                # verifica se ha itens em comum entre o grupo visitado agora e o anterior ou entre o grupo visitado agora 
                # e algum dos grupos ja visitados antes, pois assim evita um contagem em grupos em exesso por ter declarado
                # uma conexao no comeco e uma outra conexao do mesmo grupo no fim dos inputs por exemplo
                if any(item in ligacao for item in ligacoes[i-1]) or any(item in ligacao for item in lista_auxiliar):
                    pass
                else:
                    grupos += 1
        
        # adiciona o grupo visitado a lista de backup
        lista_auxiliar.extend(ligacao)
        
    return grupos

    
def main():
    # Entrada N e K
    membros, relacionamentos = [int(i) for i in input().split()]
    
    grafo = criaGrafo(membros)
    #print(grafo)
    grafo = preencheGrafo(grafo, relacionamentos)
    #print(grafo)
    grupos = countGrupos(grafo)
    print(grupos)
        

if __name__ == '__main__':
    main()
    