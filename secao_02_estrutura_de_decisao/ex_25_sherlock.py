"""
Exercício 25 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

  "Telefonou para a vítima?"
  "Esteve no local do crime?"
  "Mora perto da vítima?"
  "Devia para a vítima?"
  "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

    >>> investigar('Sim','Sim','Sim','Sim','Sim')
    'Assassino'
    >>> investigar('Sim','Sim','Sim','Sim','Não')
    'Cúmplice'
    >>> investigar('Sim','Sim','Sim','Não','Não')
    'Cúmplice'
    >>> investigar('Sim','Sim','Não','Não','Não')
    'Suspeito'
    >>> investigar('Sim','Não','Não','Não','Não')
    'Inocente'
    >>> investigar('Não','Não','Não','Não','Não')
    'Inocente'

"""


def investigar(telefonou: str, estava_no_local: str, mora_perto: str, devia: str, trabalhou: str, ):
    """Escreva aqui em baixo a sua solução"""
    perguntas = 0
    if telefonou.lower() ==  'sim':
      perguntas += 1
    if estava_no_local.lower() ==  'sim':
      perguntas += 1
    if mora_perto.lower() ==  'sim':
      perguntas += 1
    if devia.lower() ==  'sim':
      perguntas += 1
    if trabalhou.lower() ==  'sim':
      perguntas += 1

    if perguntas == 5:
      print("'Assassino'")
    elif perguntas == 3 or perguntas == 4:
      print("'Cúmplice'")
    elif perguntas == 2:
      print("'Suspeito'")
    else:
      print("'Inocente'")
    
  # --- feito ---
