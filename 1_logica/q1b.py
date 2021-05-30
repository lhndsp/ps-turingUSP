#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Lucas Hernandes da Costa Porto 
@email: lucashnds@usp.br
"""

def ordena(email: str):
    """ Ordena os emails fazendo o seguinte: recebe um email e transforma em uma lista de caracteres,
        dai separa essa lista pela metade em duas listas, e para cda uma dessas metades faz uma interacao 
        adionando a uma nova lista o caracter k-1 da respectiva metade, sendo o k o tamanho da lista, tipo
        faz praticamente uma interacao do ultimo indice ate o primeiro e vai adicionando o caracter do respectivo indice
        a uma lista, daí une essa lista em uma string, e caso o domino @usp.br esteja ok retorna o email se nao retorna ERRO
    Entrada:
        - email(str): email a ser ordanado
    Saida:
        str: email ordenado se estiver com o dominio @usp.br correto se nao ERRO
    """
    
    # transforma o email em uma lista
    email = [char for char in email]
    
    # divide a lista em duas partes, se o len() for par
    # sao duas partes iguais, se for impar a 2 parte tem um
    # caracter a mais que a primeira
    mailSize = len(email)
    
    if mailSize%2 == 1:
        delimitador = int(round(mailSize/2))
        #print(delimitador)
        email = [email[:delimitador], email[delimitador:]]
    else:
        delimitador = int(mailSize/2)
        #print(delimitador)
        email = [email[:delimitador], email[delimitador:]]
    
    # Faz um loop em cada metade dos email
    # adiconando a lista ordenadoo char na posicao 0-k,
    # ou seja, preeche a lista com o char da ultima posicao ate
    # a primeira da lista
    ordenado = []
    for mailSlice in email:
        sliceSize = len(mailSlice)
        ordenado.append([mailSlice[0-k] for k in range(1, sliceSize+1)])
    
    # unir as metades em strings e depois juntar as metades para ter o email completo
    ordenado = ''.join([''.join(i) for i in ordenado])
    
    # verifica se o dominio esta ok para o retorno
    if '@usp.br' in ordenado:
        return ordenado
    else:
        return 'ERRO'
    
    
def main():
    lenMails = int(input())
    emailOrdem = []
    for i in range(lenMails):
        emailOrdem.append(ordena(input()))
    
    for email in emailOrdem: 
        print(email)
        
        
if __name__ == '__main__':
    main()
