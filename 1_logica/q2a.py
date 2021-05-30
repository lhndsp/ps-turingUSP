#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Lucas Hernandes da Costa Porto 
@email: lucashnds@usp.br
"""

def pilha(ocorrencias, tam):
    """Faz uma interaco entre todos os instantes de entrada
       se for um valor positivo e o numero de elementos na lista ´estacionamento´
       seja menor que o tamnho digitado na entrada(indiado na variavel ´tam´): adiciona o id do carro e mantem a variavel
       ´possibilidade´ como sim, caso ao adicionar um novo item o tamanho da lista fique maior que 
       ´tam´ torna possibilidade = 'nao' e sai do loop. 
       Quanto a saida de veiculos, quando o valor for negativo, remove o ultimo item inserido em 
       ´estacionamento´ e se for igual ao modulo do do valor negativo significa que é possivel sair, entao variavel
       ´possibilidade´ é mantida como sim, caso contrario, alterada para nao e sai do loop
       
    
    Entrada:
        - ocorrencias(list) -> Instantes 
        - tam(int) -> tamanho do estacionamento
    
    Saida:
        'sim' se possivel entra e sair e 'nao' caso contrario
    """
    estacionamento = [] # nova lista para interar entr os instantes
    
    for ocorrencia in ocorrencias:
        # se for um valor positivo indica um veiculo entrando
        # entao tambem verifico se ainda cabem carro no estacionameto
        # com tamanho indicado na variavel tam, estando tudo ok mantem
        # possibilidad como sim
        if ocorrencia > 0 and len(estacionamento) <= tam:
            estacionamento.append(ocorrencia)
            possibilidade = 'sim'
        
        # se for um valor negativo indica o carro saido do estacionamento
        # entao eu removo o ultimo carro a entrar e verifico de é o mesmo
        # que esta indicado para sair, se for mantem possibilidade = sim
        elif ocorrencia < 0 and len(estacionamento) <= tam:
            ultimo = estacionamento.pop()
            if ultimo == abs(ocorrencia):
                possibilidade = 'sim'
            else:
                possibilidade = 'nao'
                break
                
        # caso nao tenha mais espaco no estacionamento retorna nao
        else:
            possibilidade = 'nao'
            break
            
    return possibilidade


def main():
    # tamanho do estacionamento e numero de instantes
    K, N = tuple([int(i) for i in input().split()])
    
    # adiciona o numero de ocorrencias = N
    instantes = [int(input()) for i in range(N)]
    
    p = pilha(instantes, K)
    print(p)
    
    
if __name__ == '__main__':
    main()

