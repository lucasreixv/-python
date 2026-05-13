#FUNÇÕES

#aqui a função def esta calculando o valor dentro dos parâmetros, vai retornar multiplicando
def calcular_subtotal(preço, quantidade):
    return preço * quantidade

#abaixo estao as equações de desconto

def aplicar_desconto(total):
    if total >= 1000:
        return total * 0.85
    elif total >=500:
        return total * 0.90
    elif total >= 200:
        return total *0.95
    else:
        return total
    
#aqui esta calculando a media das vendas, o total é a soma de todas as vendas e quantidade é o número de vendas
def calcular_media(total, quantidade):
    if quantidade == 0: #isso aq evita erro de matematica, dividir por zero da erro
        return 0
    return total / quantidade
    
#essa função aqui encontra qual cliente gastou mais:
def maior_compra(vendas):
    maior = vendas[0] #começa assumindo que o primeiro é o maior
    for venda in vendas: #percorre todas as vendas
        if venda["total"] > maior ["total"]: #aqui compara, se encontrar uma venda maior, ele atualiza
            maior = venda
    return maior  # corrigi

#CADASTRO DE PRODUTOS:

produtos = []

while True:
    print("\nCadastro de Produto")

    nome = input("Nome do produto: ")
    preço = float(input("Preço: "))
    estoque = int(input("Estoque: "))

    produto = {
        "nome" : nome,
        "preço" : preço,
        "estoque" : estoque
    }
    
    produtos.append(produto)

    continuar = input("Cadastrar outro produto? (s/n: )")
    if continuar != "s":
        break

#Sistema de vendas:

vendas = []

while True:
    print("\nNova venda")

    nome_cliente = input("Nome do cliente: ")
    total = 0

    while True:
        nome_produto = input("Produto : ")

        produto_encontrado = None

        for produto in produtos:
            if produto["nome"].lower() == nome_produto.lower():
                produto_encontrado = produto
                break

        if produto_encontrado is None:
            print("Produto não encontrado")
        else:
            quantidade = int(input("Quantidade: "))
            if quantidade > produto_encontrado["estoque"]:
                print("Estoque insuficiente")

            else: 
                subtotal = calcular_subtotal(produto_encontrado["preço"], quantidade)

                produto_encontrado["estoque"] -=quantidade
                total += subtotal

                print(f"Subtotal: {subtotal}")

        continuar_compra = input("Adicionar mais produtos? (s/n): ")  #corrig, estava dentro do else
        if continuar_compra != "s":
            break

    # salvando a venda
    total = aplicar_desconto(total)

    venda = {
        "cliente": nome_cliente,
        "total": total
    }

    vendas.append(venda)

    continuar_venda = input("Realizar outra venda? (s/n): ")  # loop infinito resolvido
    if continuar_venda != "s":
        break


#Relatório Final:

total_vendas = len(vendas)

rendimento_total = 0
for venda in vendas:
    rendimento_total += venda["total"]

media = calcular_media(rendimento_total, total_vendas)

if total_vendas >0:
    maior = maior_compra(vendas)
else:
    maior = None

#Exibindo informações:
print("\nResumo das vendas: ")
for venda in vendas:
    print(f"Cliente: {venda['cliente']} | Total: {venda['total']}")
    
print("\n-Geral-: ")
print(f"Total de vendas: {total_vendas}")
print(f"Rendimento total: {rendimento_total}")
print(f"Média das vendas: {media}")

if maior: 
    print(f"Maior compra: {maior['cliente']} - {maior['total']} ")