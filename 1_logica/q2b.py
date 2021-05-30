#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Lucas Hernandes da Costa Porto 
@email: lucashnds@usp.br
"""

## Eu tambem deixei explicado a minha logica em um diagrama
## na imagem: exlicacao_q2b.png
## acho que consigui explicar melhor nela

class Fila(object):
    """ 1) Cria uma lista ´estacionamento´ de zeros de tamanha ´tam´
        2) cria uma lista ´fila´ de zeos de tamanho ´interesse´
        3) para cada instante t na entrada ´instantes´, substitui na lista ´estacionamento´ no indicie
           t - 1 (para normalizar com a indexacao da lista) o valor do index do 
           respectivo t
        4) 
    """
    def __init__(self, tam, instantes, interesse):
        self.estacionamento = [0]*tam
        self.instantes = instantes
        self.final = interesse
        if max(instantes) < interesse:
            self.fila = [0]*interesse 
        else:
            self.fila = [0]*max(instantes)

    def preencheFila(self):
        for j, i in enumerate(self.instantes):
            self.fila[i-1] = j+1
        print(self.fila)
        
    def mover(self):
        k = 0
        while k < self.final:
            n = self.fila.pop()
            self.estacionamento.insert(0, n)
            self.estacionamento.pop()
            k += 1
    #def __repr__(self):
    #    return self.estacionamento
    
    def gerenciaFila(self):
        self.preencheFila()
        self.fila = self.fila[::-1]
        print(self.fila)
        self.mover()
        return self.estacionamento
        
def main():
    # tamanho do estacionamento e numero de carros
    K, N = tuple([int(i) for i in input().split()])
    
    # adiciona o numero de ocorrencias = N
    entrada = [int(input()) for i in range(N)]
    
    # instante de interesse
    tf = int(input())
        
    fila = Fila(tam=K, 
                instantes=entrada,
                interesse=tf)
    
    print(fila.gerenciaFila())
    
if __name__ == '__main__':
    main()

