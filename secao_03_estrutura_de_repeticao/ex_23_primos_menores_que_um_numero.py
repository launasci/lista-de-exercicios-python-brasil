"""
Exercício 23 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

    >>> primos, divisoes = calcular_primos_e_divisoes(0)
    >>> primos
    ''
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(1)
    >>> primos
    ''
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(2)
    >>> primos
    '2'
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(3)
    >>> primos
    '2, 3'
    >>> divisoes <= 1
    True
    >>> primos, divisoes = calcular_primos_e_divisoes(4)
    >>> primos
    '2, 3'
    >>> divisoes <= 3
    True
    >>> primos, divisoes = calcular_primos_e_divisoes(5)
    >>> primos
    '2, 3, 5'
    >>> divisoes <= 6
    True

"""
from typing import Tuple


def calcular_primos_e_divisoes(n: int) -> Tuple[str, int]:
    """Escreva aqui em baixo a sua solução"""
    div = 0 
    numeros = list(range(3, n+1))
    primos = list()
    if n > 1:
        primos = [2]
        for numero in numeros:
            rep = 0 
            for num in range( 1, numero + 1):
                if numero % num == 0:
                    rep += 1
            if rep == 2:
                primos.append(numero)
                div += 1
    primos = str (primos)
    primos = primos [1:-1]
    return(primos, div)
# -- feito --

