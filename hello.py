#!/usr/bin/env python
# todas as variaveis de ambiente vão para o python rodar o programa

"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa existe a 
mensagem correspondente

Como usar:

Tenha a variável LANG devidamente configurada ex:
    export LANG=pt_BR

Execução:
    python hello.py
    ou
    ./hello.py
"""

# Metados
__version__ = "0.0.1"
__author__ =  "Fernando C Fabril"
__license__ = "Unlicense"

# Dunder = double underline

import os

# pega a variavel de ambiente LANG, até os 5 primeiros caracteres
# se a variavel de ambiente não estiver definida, define o valor
# padrão "pt_BR"
current_language = os.getenv("LANG", "pt_BR")[:5]
msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "ex_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

# Define o bloco principal de um programa python
if __name__ == "__main__":
    print(msg)
