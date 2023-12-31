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

__version__ = "0.2.0"

from datetime import datetime
import os
import sys
arguments = sys.argv[1:]

if not arguments:
    operation = input("operação: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
elif len(arguments) != 3:
    print("Número de argumetnos inválidos")
    print("ex: `sum 5 5`")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operação inválida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    # TODO: Repetição while + exceptions
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums

# TODO: Usar dict de funções
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

print(f"O resultado da operação é = {result}")

path = os.curdir
filepath = os.path.join(path, "prefixcalc.log")
timestamp
