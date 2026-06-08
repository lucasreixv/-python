

class Produto:

    def __init__(self, nome, preco):  #"init" e um modo construtor
        self.nome = nome  #self : guarda um obleto
        self.preco = preco

    def exibir(self):
        print(f"{self.nome} - R$ {self.preco:.2f}")


produtos = [] # cria uma lista


def cadastrar_produto():

    nome = input("Nome do produto: ")

    try:

        preco = float(input("Preço do produto: ").replace(",", "."))

        if preco < 0:
            print("Preço inválido!")

        else:

            produto = Produto(nome, preco)

            produtos.append(produto)

            print("Produto cadastrado com sucesso!")

    except ValueError:

        print("Digite um preço válido!")




def listar_produtos():

    if len(produtos) == 0:

        print("Nenhum produto cadastrado!")

    else:

        print("\nLISTA DE PRODUTOS")

        for indice, produto in enumerate(produtos):

            print(f"{indice} - {produto.nome} - R$ {produto.preco:.2f}")


def comprar_produto():

    if len(produtos) == 0:

        print("Nenhum produto cadastrado!")

    else:

        listar_produtos()

        try:

            indice = int(input("Digite o número do produto: "))

            produto = produtos[indice]

            quantidade = int(input("Quantidade: "))

            total = produto.preco * quantidade

            print(f"Total da compra: R$ {total:.2f}")

            if total >= 100:

                print("Desconto disponível")

            else:

                print("Sem desconto")

        except ValueError:

            print("Digite apenas números!")

        except IndexError:

            print("Produto inexistente!")


while True:

    print("\n===== MENU =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Comprar produto")
    print("4 - Sair")

    try:

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:

            cadastrar_produto()

        elif opcao == 2:

            listar_produtos()

        elif opcao == 3:

            comprar_produto()

        elif opcao == 4:

            print("Programa encerrado!")
            break

        else:

            print("Opção inválida!")

    except ValueError:

        print("Digite apenas números!")