#!/usr/bin/python3
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
    Contagem de micro grupos no grafo
    
    Entrada:
        grafo (dict) -> {'vertice 1':[conexao 1, conexao 2, ..., conexao n], ..., 
                         'vertice n':[conexao 1, conexao 2, ..., conexao n]}
                        criado em preencheGrafo()
    Saida:
        (int) -> Numero de grupos
    """
    # {1: [2, 3], 
    #  2: [1, 3], 
    #  3: [2, 1, 4], 
    #  4: [3], 
    #
    #  5: [6, 7], 
    #  6: [5], 
    #  7: [5]}
    
    ligacoes = []
    
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
                if any(item in ligacao for item in ligacoes[i-1]):
                    pass
                else:
                    grupos += 1
    
    return grupos

    
def main():
    # Entrada N e K
    membros, relacionamentos = [int(i) for i in input().split()]
    
    grafo = criaGrafo(membros)
    #print(grafo)
    grafo = preencheGrafo(grafo, relacionamentos)
    print(grafo)
    grupos = countGrupos(grafo)
    print(grupos)
        

if __name__ == '__main__':
    main()
    