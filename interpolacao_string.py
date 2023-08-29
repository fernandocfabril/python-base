# https://pyformat.info

email_tmpl = """
    Olá, %(nome)s

    Tem interesse em comprar o %(produto)s?

    Este produto é ótimo para resolver
    %(texto)s

    Clique agora em %(link)s

    Apenas %(quantidade)03d disponiveis!

    Preço promocional %(preco).2f
    """

clientes = ["Maria", "Joao", "Bruno"]

for cliente in clientes:
    print(
        email_tmpl
        %{
            "nome": cliente,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "https://canetaslegais.com",
            "quantidade": 2,
            "preco": 50.5236
        }
    )