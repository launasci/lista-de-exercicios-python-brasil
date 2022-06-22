"""
Exercício 15 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o
n−ésimo termo.

    >>> calcular_serie_de_fibonacci(1)
    '1'
    >>> calcular_serie_de_fibonacci(2)
    '1, 1'
    >>> calcular_serie_de_fibonacci(3)
    '1, 1, 2'
    >>> calcular_serie_de_fibonacci(4)
    '1, 1, 2, 3'
    >>> calcular_serie_de_fibonacci(5)
    '1, 1, 2, 3, 5'
    >>> calcular_serie_de_fibonacci(6)
    '1, 1, 2, 3, 5, 8'
    >>> calcular_serie_de_fibonacci(7)
    '1, 1, 2, 3, 5, 8, 13'

"""


def calcular_serie_de_fibonacci(n: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    ultimo = 1
    penultimo = 1
    soma = 1
    if n == 1:
        print(f"'{n}'")    
    else:
        n -= 1
        print("'1", end=", ")
        for numero in range(n):
            if numero == n -1:
                print(f"{soma}'", end="")
            else:
                print(f"{soma}", end=", ")
                soma = ultimo + penultimo
                ultimo = penultimo
                penultimo = soma


#     ultimo = 1
#     penultimo = 1
#     termo = 1
#     if n == 1:
#         print("'1'")
#     else:
#         n -= 1
#         print("'1", end=', ')
#         for batata in range(n):
#             if batata == n-1:
#                 print(f"{termo}'")
#             else:
#                 print(termo, end=', ')
#                 termo = penultimo + ultimo
#                 ultimo = penultimo
#                 penultimo = termo
# #  --- feito -

    # n1 = 1
    # n2 = 1
    # n3 = 1
    # if n == 1:
    #     print (f"'{n}'")
    # else:
    #     n -= 1
    #     print("'1", end=", ")
    #     for i in range (n):
    #         if i == n-1:
    #             print(f"{n3}'", end='') 
    #         else:
    #             print (f"{n3}", end=", ")
    #             n3 = n1 + n2
    #             n1 = n2
    #             n2 = n3
