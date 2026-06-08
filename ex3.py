produtos = []

qtd = int(input("Quantos produtos? "))

for i in range(qtd):
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    estoque = int(input("Estoque: "))
    
    produtos.append([nome, preco, estoque])
#Cada .append() coloca algo no fim da lista
vendas = []

resp_venda = "s"

while resp_venda != "n":
    cliente = input("\nCliente: ")
    total = 0
    
    resp = "s"
    
    while resp != "n":
        nome_prod = input("Produto: ")
        
        achou = False
        #Cada p é um produto inteiro, a posição começa em 0
    for p in produtos:
        nome = p[0]
        preco = p[1]
        estoque = p[2]
        if nome == nome_prod:
            achou = True
            qtd = int(input("Quantidade: "))
            if qtd <= estoque:
                subtotal = qtd * preco
                total += subtotal
                p[2] = estoque - qtd  # atualiza estoque
                print("Subtotal:", subtotal)
            else:
               print("Sem estoque!")
               if not achou:
                   print("Produto não existe!")
                   resp = input("Continuar compra? (S/N): ")
    
    
    # DESCONTO (simples)
    if total >= 1000:
        desc = total * 0.15
    elif total >= 500:
        desc = total * 0.10
    elif total >= 200:
        desc = total * 0.05
    else:
        desc = 0
    
    final = total - desc
    
    vendas.append([cliente, final])
    
    print("Total final:", final)
    
    resp_venda = input("Nova venda? (s/n): ")



total_loja = 0
maior = 0
melhor_cliente = ""

for v in vendas:
    total_loja += v[1]
    
    if v[1] > maior:
        maior = v[1]
        melhor_cliente = v[0]

if (vendas) > 0:
    media = total_loja / (vendas)
else:
    media = 0

print("RELATÓRIO")
print("Total de vendas:", (vendas))
print("Faturamento:", total_loja)
print("Média:", media)
print("Quem mais comprou:", melhor_cliente)