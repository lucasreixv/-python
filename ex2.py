
def calcular_desconto(total):
    if total >= 1000:
        return total * 0.15
    elif total >= 500:
        return total * 0.10
    elif total >= 200:
        return total * 0.05
    else:
        return 0

quantidade = int(input("Quantos produtos deseja cadastrar? "))

produtos = [None] * quantidade
#none = espaço vazio esperando valor
for i in range(quantidade):
    print("Produto", i+1)
    
    nome = input("Nome: ")
    preco = float(input("Preco: "))
    estoque = int(input("Estoque: "))
    
    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }
    
    produtos[i] = produto

cliente = input("Nome do cliente: ")

total = 0

continuar = "s"

while continuar != "n":
#! singnifica diferte de N continua
    
    nome_produto = input("\nDigite o nome do produto: ")
    
    encontrado = False
    
    for produto in produtos:
        if produto["nome"] == nome_produto:
            encontrado = True
            
            quantidade_compra = int(input("Quantidade: "))
            
            if quantidade_compra <= produto["estoque"]:
                
                subtotal = quantidade_compra * produto["preco"]
                
                produto["estoque"] = produto["estoque"] - quantidade_compra
                
                total = total + subtotal
                
                print("Item adicionado. Subtotal:", subtotal)
            else:
                print("Estoque insuficiente")
    
    if encontrado == False:
        print("Produto nao encontrado")
    
    continuar = input("Deseja continuar? (S/N): ")


desconto = calcular_desconto(total)

total_final = total - desconto


print("Resultado final")
print("Cliente:", cliente)
print("Total:", total)
print("Desconto:", desconto)
print("Total final:", total_final)