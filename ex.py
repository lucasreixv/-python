while True:
    print("NOVA VENDA")
    nome_cliente = input("Digite o nome do cliente: ")
    qtd_produtos = int(input("Quantos produtos serão comprados?"))
    total = 0
    for i in range(qtd_produtos):
        print (f"produto {i+1}")
        nome_produto = input ("nome do produto: ")
        preço = float (input("Preço: "))
        quantidade = int(input("Quantidade: "))
        subtotal = preço * quantidade 
        print(f"{subtotal: .2f}")

        total+=subtotal
    if total >=500:
        desconto = total *0.104
    elif total >= 200:
        desconto = total *0.05
    else:
        desconto = 0
    total_final = total - desconto

    print ("RESUMO")
    print (f"Cliente {nome_cliente}")
    print (f" Total: R$ {total: .2f}")
    print (f" Desconto: R$ {desconto: .2f}")
    print (F" Total final: R$ {total_final: .2f}")

    continuar = input("Deseja fazer outra venda? Responda com S ou N: ").upper()
    if continuar == "N":
        print ("ENCERRANDO SISTEMA")
        break