"""
Exercício 48 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  entrada => 12376489
  saida => 98467321

    >>> inverter_inteiro(0)
    0
    >>> inverter_inteiro(123456789)
    987654321
    >>> inverter_inteiro(3454232311243232979128123)
    3218219792323421132324543
    >>> inverter_inteiro(987654321)
    123456789

"""


from audioop import reverse


def inverter_inteiro(numero):
    """Escreva aqui em baixo a sua solução"""
    numero = str(numero)[:: -1]
    print(numero)
    
    # -- feito --
    # Então, quando você faz numero[::-1], começa do final para o primeiro, 
    # pegando cada elemento. Então inverte numero. 
    # Isso também é aplicável para listas/tuplas.