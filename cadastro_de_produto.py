#1/usr/bin/env python
"""Cadastro de produto"""
__version__ = "0.1.0"

from pprint import pprint

produto = {
    "nome": "Caneta",
    "cores": ["azul", "branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None,
}

cliente = {
    "nome": "Fernando"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}

total_compra = compra["quantidade"] * compra["produto"]["preco"]

#pprint(compra)

print(
    f"O cliente {compra['cliente']['nome']}\n"
    f"comprou o produto {compra['produto']['nome']}\n"
    f"e pagou o total de {total_compra}"
)