#INTEGRADOR - SISTEMA DE CADASTRO E COMPRA

class Produto:
    def __init__(self , nome ,preço):
        self.nome = nome
        self.preço = preço
        
    def mostrar (self):
        print(f"Produto: {self.nome} | Preço: {self.preço}")



def aplicar_desconto(total):
    
    if total >= 100:
        return print("Você possui desconto!")

    else:
        return print("Você não possui desconto!")
    
#essa função serve pra procurar o produto pelo nome dentro da lista
def buscar_produto(produtos):

    if len(produtos)==0:
        print("Não há produtos cadastrados")
    
    else:
        print(produtos)



# p1 = Produto('nome', 'preço')
#p1.mostrar()

produtos = []
vendas = []

while True:
    
    print("\n1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Comprar produto")
    print("4 - Relatório final")
    print("5 - Sair")

    try:

        opção = int(input("Escolha: "))

    except:

        print("Digite apenas números!")
        continue

            #OPÇÃO DE CADASTRO DE PRODUTOSS (1)

    if opção == 1:
    
        nome = input("Nome do produto: ")

        try:

            preco = float(input("Preço: ").replace(",", "."))
            if preco < 0:
                print("Valor inválido!")

            else:
                produto = Produto(nome, preco,)
                produtos.append(produto)

                print("Produto cadastrado!")

        except ValueError:

            print("Erro! Digite valores válidos.")
            #LISTANDO PRODUTOS:]

    elif opção == 2:
        produto.mostrar()


    elif opção ==3:
        print("\nProdutos disponíveis:")

        #aqui ele percorre a lista e mostra todos os produtos toda vez que for comprar
        for produto in produtos:
        
            print(f"Produto: {produto['nome']} , Preço: {produto['preço']} , Estoque: {produto['estoque']}")

        nome_produto = input("Qual produto deseja comprar?: ")

        #aqui ele tenta encontrar o produto digitado
        produto_encontrado = buscar_produto(produtos, nome_produto)

        if produto_encontrado is None:

            print("Produto não encontrado")

        else:



          
            



