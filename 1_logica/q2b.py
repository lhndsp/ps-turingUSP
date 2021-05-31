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
    def __init__(self, tam, instantes, interesse):
        # cria uma lista representando estacinamento, por default vazio (com 0s)
        self.estacionamento = [0]*tam 
        
        # a lista com os instantes digitados na entrada, sendo que o 
        # index + 1 da lista representa o id do carro
        self.instantes = instantes 
        
        # o instante aser observado
        self.final = interesse
        
        # cria a fila de carros, a principio com 0s a srem substituidos depois
        # se o instante de interesse for maior que o numero de carros a entrar
        # representado por ´tam´ cria uma lista de tamanho ´tam´ pois mesmo
        # depois de acabarem os carros as observacoes continuam
        # se for menor entao cria lista do tamanho de instantes
        if max(instantes) < interesse:
            self.fila = [0]*interesse 
        else:
            self.fila = [0]*max(instantes)

            
    def preencheFila(self):
        """ a fila de carros por default é preenchida de 0, e cada index representa o instante
            e o valor do element no index o id do carro, essa funcao vai alterar na fila de 
            carros nos respectivos indexes referentes aos digitados na entrada, com o id do 
            resectivo carro
        """
        for j, i in enumerate(self.instantes):
            self.fila[i-1] = j+1
        print(self.fila)
        
        
    def mover(self):
        """ usando o exemplo 2 do enunciado:
            com a fila de carros = [0, 0, 1, 5, 0, 2, 0, 0, 4, 0, 0, 3, 0, 0, 6, 7]
            o estacionameto estaria de seguinte forma do instante 1 ate o instante
            de interesse:
            [0, 0, 0, 0, 0] {instante 1}
            [0, 0, 0, 0, 0] {instante 2}
            [1, 0, 0, 0, 0] {instante 3}
            [5, 1, 0, 0, 0] {instante 4}
            [0, 5, 1, 0, 0] {instante 5}
            [2, 0, 5, 1, 0] {instante 6}
            [0, 2, 0, 5, 1] {instante 7}
        """
        
        k = 0
        while k < self.final:
            n = self.fila.pop()
            self.estacionamento.insert(0, n)
            self.estacionamento.pop()
            k += 1
            
            
    #def __repr__(self):
    #    return self.estacionamento
    
    
    def gerenciaFila(self):
        """
        executa as funcoes acima e retorna o estado do instacionameto
        decorrido no instante de ineteresse
        """
        self.preencheFila()
        self.fila = self.fila[::-1] # inverte a ordem da fila pois o primeiro a entrar é o primeiro a sair
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

