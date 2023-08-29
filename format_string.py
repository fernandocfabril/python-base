# https://pyformat.info

email_tmpl = """
    Olá, {nome}

    Tem interesse em comprar o {produto}?

    Este produto é ótimo para resolver
    {texto}

    Clique agora em {link}

    Apenas {quantidade:03d} disponiveis!

    Preço promocional {preco:.2f}
    """

clientes = ["Maria", "Joao", "Bruno"]

for cliente in clientes:
    print(
        email_tmpl.format(
            nome=cliente, 
            produto="caneta", 
            texto="Escrever muito bem",
            link="https://canetaslegais.com",
            quantidade=2,
            preco=50.5236           
            )
    )