"""
Exercício 39 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o nome do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o nome do aluno mais alto
 e o número do aluno mais baixo, junto com suas alturas.
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162))
    'O maior aluno é o Renzo com 162 cm. O menor aluno é o Renzo com 162 cm'
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162), ('Clara', 165))
    'O maior aluno é o Clara com 165 cm. O menor aluno é o Renzo com 162 cm'
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162), ('Clara', 165), ('Oscar', 199))
    'O maior aluno é o Oscar com 199 cm. O menor aluno é o Renzo com 162 cm'

"""


def calcular_aluno_mais_baixo_e_mais_alto(*alunos) -> str:
    """Escreva aqui em baixo a sua solução"""
    nome_maisalto = nome_maisbaixo = ''
    altura_maisalto = 0
    altura_maisbaixo = 1000
    for (nome, altura) in alunos:
        if altura > altura_maisalto:
            altura_maisalto = altura 
            nome_maisalto = nome 
        if altura < altura_maisbaixo:
            altura_maisbaixo = altura
            nome_maisbaixo = nome
    print(f"'O maior aluno é o {nome_maisalto} com {altura_maisalto} cm. O menor aluno é o {nome_maisbaixo} com {altura_maisbaixo} cm'")

    # -- feito -- 
        


