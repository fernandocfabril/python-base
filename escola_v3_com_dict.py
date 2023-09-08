#!/usr/bin/env python

"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das ativiades
"""
__version__ = "0.1.0"

# Listar alunos em cada atividade por sala

salas = {
    1: ["Erick", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    2: ["Joao", "Antonio", "Carlos", "Antonio"]
}

atividades = {
    "ingles": ["Erick", "Maia", "Joana", "Carlos", "Antonio"],
    "musica": ["Erick", "Carlos", "Maria"],
    "danca": ["Gustavo", "Sofia", "Joana", "Antonio"] 
}

for nome_atividade, aluno_atividade in atividades.items():
    print(f"Alunos da atividade {nome_atividade}")
    print("-" * 40)

    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in aluno_atividade:
        if aluno in salas[1]:
            atividade_sala1.append(aluno)
        elif aluno in salas[2]:
            atividade_sala2.append(aluno)

    print(f"Atividade de {nome_atividade} da Sala1 {atividade_sala1}")
    print(f"Atividade de {nome_atividade} da Sala2 {atividade_sala2}")

    print("#" * 40)
    print()