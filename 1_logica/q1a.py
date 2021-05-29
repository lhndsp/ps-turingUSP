#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: Lucas Hernandes da Costa Porto 
@email: lucashnds@usp.br
"""

def comparacao(emails: list, k: int):
    """comparacao da entrada atual com a penultima, e contagem
    dos caracteres ue podem ser economizados entre ambas

    Parametros:
        - emails (list): lista com dois elementos: o email atual e o penultimo 
        - k (int): indicie atual da lista
    Saida:
        (int): numero de caracteres economizados na comparacao dos dois email 
    """
    # Elimina o dominio @usp.br
    emails = [i.replace('@usp.br', '') for i in emails]

    # transforma a string em uma lista de caracteres, equivalende ao str.split() *N sabia se podia usar
    # assim vai a entrada x vai ficar [['c1', 'c2', ..., 'cn'], ['c1', 'c2', ..., 'cn']]
    emails = [[char for char in email] for email  in emails]
    
    n = 0 # numero de caracteres a se economizar no email atual
    
    if k == 0:
        pass # Nao elimia nada no primeiro email
    else:
        for i, char in enumerate(emails[k]):
            if emails[k-1][i] == char:
                n += 1
            else:
                break
    
    return n


def main():
    lenMails = int(input())
    mailList = []
    economia = []
    for i in range(lenMails):
        mailList.append(input())
        economia.append(comparacao(emails=mailList, k=i))
    print(sum(economia))

if __name__ == '__main__':
    main()