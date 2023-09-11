#!/usr/bin/env python
"""Calcularoa prefix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> - 
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcal.py
operação: sum
n1: 5
n2: 4
9
"""

__version__ = "0.1.0"

import sys

arguments = sys.argv[1:]

operadores = {
    "sum": "+",
    "sub": "-",
    "mul": "*",
    "div": "/'"
}

if len(arguments) == 0:
    operacao = input("operação: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
else:
    operacao, n1, n2 = arguments

n1 = int(n1)
n2 = int(n2)

if operacao == "sum":
    result = n1 + n2
elif operacao == "sub":
    result = n1 - n2
elif operacao == "mul":
    result = n1 * n2
elif operacao == "div":
    result = n1 / n2
else:
    print("Operação invalida!")
    sys.exit()

print(f"O resultado da operação '{operacao} {n1} {n2}' é = {result}")
