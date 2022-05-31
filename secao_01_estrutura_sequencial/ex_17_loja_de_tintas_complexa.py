"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""


import math


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    metros =input('Informa a área a ser pintada:')
    lata = 18
    litros = (metros/6)+(metros/6)*0.1
    Qtde_latas = math.ceil(litros/18)
    sobra = (Qtde_latas*18)- litros
    preço_lata = Qtde_latas*80
    qtde_galao = math.ceil(litros/3.6)
    sobra_galao = (qtde_galao*3.6) - litros
    preço_galao = qtde_galao*25
    qtde_latas_nv = (litros/lata)
    sobra_ml = (qtde_latas_nv - math.trunc(qtde_latas_nv))*lata
    qtde_galao_nv = sobra_ml



    
    # lata=18
    # galao=3.6
    # metros=float(input('Informa a área a ser pintada:'))
    # litros=((metros/6)*2)*0.10
    # quantidade_lata=math.ceil(litros/lata)
    # quantidade_galao=math.ceil(litros/galao)
    # sobra_lata=(quantidade_lata*lata)-litros
    # sobra_galao=(quantidade_galao*galao)-litros
    # preco_lata=quantidade_lata*80
    # preco_galao=quantidade_galao*25
    # print(f'Você deve comprar {litros} litros de tinta.')
    # print(f'Você pode comprar {quantidade_lata} lata(s) de 18 litros a um custo de R$ {preco_lata}. Vão sobrar {sobra_lata} litro(s) de tinta.')
    # print(f'Você pode comprar {quantidade_galao} lata(s) de 3.6 litros a um custo de R$ {preco_galao}. Vão sobrar {sobra_galao} litro(s) de tinta.')
    # print(f'Para menor custo, você pode comprar {} lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ {}. Vão sobrar {} litro(s) de tinta.')
    


   

    