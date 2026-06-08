while True:
    print("NOVA VENDA")

    nome_cliente = input("Nome do cliente: ")
    qtd_produtos = int(input("Quantidade de produtos: "))

    total=0

    for i in range(qtd_produtos):
        print("Produto", i + 1)
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
#i posiçao atual do produto
        subtotal = preco * quantidade
        total = total + subtotal   

    if total >= 500:
        desconto = total * 0.1
    else:
        if total >= 200:
            desconto = total * 0.05
        else:
            desconto = 0

    total_final = total - desconto

    print(" RESUMO ")
    print("Cliente:", nome_cliente)
    print("Produtos:", nome)
    print("Total:", total)
    print("Desconto:", desconto)
    print("Total final:", total_final)

    continuar = input("Outra venda? (s/n): ")

    if continuar == "n":
        break