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
    metros_quadrado=float(input('Informe a área a ser pintada:'))
    metros_litros=metros_quadrado*1.1
    litros=math.ceil(metros_litros/6)
    latas=math.ceil(litros/18)
    galao=math.ceil(litros/3.6)
    preco_lata=latas*80
    preco_galao=galao*25
    rest_latas=(latas*18)-litros
    rest_galao=(galao*3.6)-litros
    resto=litros%18 
    latas_int=math.floor(litros/18)
    galao_rest=math.ceil(resto/3.6) 
    latas_custo=latas_int*80
    galao_custo=galao_rest*25
    latas_e_galoes=((latas_int*80)+(galao_rest*25))
    resto_total=((latas_int*18)+(galao_rest*3.6))-litros 
    print(f'Você deve comprar {litros} litros de tinta.')
    print(f'Você pode comprar {latas} lata(s) de 18 litros a um custo de R$ {preco_lata}. Vão sobrar {rest_latas:.1f} litro(s) de tinta.')
    print(f'Você pode comprar {galao} lata(s) de 3.6 litros a um custo de R$ {preco_galao}. Vão sobrar {rest_galao:.1f} litro(s) de tinta.')
    print(f'Para menor custo, você pode comprar {latas_int} lata(s) de 18 litros e {galao_rest} galão(ões) de 3.6 litros a um custo de R$ {latas_e_galoes:.0f}. Vão sobrar {resto_total:.1f} litro(s) de tinta.')

# ------------ santo deus -------------