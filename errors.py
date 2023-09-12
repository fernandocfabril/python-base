#!/usr/bin/env python
import os
import sys

try:
    names = open("names.txt").readlines()
except FileNotFoundError as e:
    print(f"{str(e)}")
    sys.exit(1)
else:
    # executa o else quando não da erro
    print("Sucesso!!!")
finally:
    # sempre executa mesmo dando erro
    print("Final!!!")

try:
    print(names[2])
except:
    print("[Erro] Missing name in the list")
    sys.exit(1)

