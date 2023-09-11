#!/user/bin/env python
""" Imprime a mensagem de um e-mail
"""

# https://pyformat.info

import os
import sys

arguments = sys.argv[1:]
if not arguments:
    print("Informar o nome do arquivo de e-mails e do template")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)


for line in open(filepath):
    name, email = line.split(",")

    print(f"Enviando e-mail para {email}")
    print(
        open(templatepath).read()
        %{
            "nome": name,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "https://canetaslegais.com",
            "quantidade": 2,
            "preco": 50.5236
        }
    )
    print("-" * 50)
    print()