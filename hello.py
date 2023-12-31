#!/usr/bin/env python
# todas as variaveis de ambiente vão para o python rodar o programa

"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa existe a 
mensagem correspondente

Como usar:

Tenha a variável LANG devidamente configurada ex:
    export LANG=pt_BR

Execução:
    python hello.py --lang=pt_BR
    ou
    ./hello.py --lang=pt_BR

"""

# Metados
__version__ = "0.0.1"
__author__ =  "Fernando C Fabril"
__license__ = "Unlicense"

# Dunder = double underline

import os
import sys

arguments = {
    "lang": None,
    "count": 1,
}
# pega os arqumentos a partir da posição 1
for arg in sys.argv[1:]:
    # TODO: Tratar ValueErro
    try:
        # desempacotar
        key, value = arg.split("=")
    except ValueError as e:
        print(f"[ERROR] {str(e)}")
        print("You nee use --key=value")
        sys.exit(1)

    # remove todos os "-" a esquerda do argumento
    # transforma o argumento em minusculo
    # elimina os espaçoes em branco
    key = key.lstrip("-").lower().strip()
    # elimina os espaçoes em branco
    value = value.strip()
    print(f"{key} -> {value}")
    if key not in arguments:
        print(f"Invalid options '{key}'")
        # aborta o programa
        sys.exit()
    arguments[key] = value

    

# pega a variavel de ambiente LANG, até os 5 primeiros caracteres
# se a variavel de ambiente não estiver definida, define o valor
# padrão "pt_BR"
current_language = arguments["lang"]
if current_language == None:
    # verifica se LANG existe nas variaveis de ambiente
    if 'LANG' in os.environ:
        current_language = os.getenv("LANG", "pt_BR")
    else: # pedi para o usuário digitar uma linguagem
        current_language = input("Choose a language: ")

# pega as 5 primeiras posições    
current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mondo!",
    "fr_FR": "Bonjour, Monde!"
}

# msg = "Hello, World!"
# if current_language == "pt_BR":
#     msg = "Olá, Mundo!"
# elif current_language == "it_IT":
#     msg = "Ciao, Mondo!"
# elif current_language == "ex_SP":
#     msg = "Hola, Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjour, Monde!"

# Define o bloco principal de um programa python
if __name__ == "__main__":
    try:
        message = msg[current_language]
    except KeyError as e:
        print(f"[ERROR] {str(e)}")
        print(f"Language is invalid, choose from: {list(msg.keys())}")
        sys.exit(1)

""" 
uma alternativa ao try execpt seria usar o comando:

message = msg.get(current_language, msg["en_US])

nesse caso tenta buscar a current_language e se não achar
traz um valor padrão.

isso é possível em dicionários utilizando o comando get
"""

    print(message * int(arguments["count"]))
