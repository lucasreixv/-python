# CLASSE CLIENTE
import os #importa a biblioteca os, que serve para trabalhar com arquivos e pastas

ARQUIVO = r"C:\Users\1bmod\Documents\manuelucas.py\cliente.TXT" #guarda o caminho onde o arquivo clientes.txt vai ser salvo
# r significa raw string, para o python entender as barras \ corretamente

CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
LIGHT_BLUE = "\033[94m"
LIGHT_PINK = "\033[38;5;218m"
PINK = "\033[95m"       # Magenta claro (parece rosa em muitos terminais)
HOT_PINK = "\033[38;5;205m"  # Rosa choque (256 cores)
RESET = "\033[0m"
ORANGE = "\033[38;5;208m"


class Cliente: #criando uma classe chamada cliente, o molde
    def __init__(self, nome, idade, email, telefone): # é executado automaticamente quando a gente cria um objeto da classe, o metodo construtor feito para inicializar o objeto com os dados qe ele preicsa ter ao ser criado
        self.nome = nome #self representa o próprio objeto que está executando o método.
        self.idade = idade
        self.email = email #atriibutes da classe, sao os dados do objeto
        self.telefone = telefone

    def mostrar(self): #mostrar é um metodo da classe, uma função que pertence aos objetos da classe
        print(f"Nome: {self.nome}") #todos esses sao instancias criadas a partir da classe
        print(f"Idade: {self.idade}") #f permite por variaveis dentro de um texto
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print("--------------------------------------")

# CLASSE SISTEMA

class SistemaCadastro: #apenas criando

    def __init__(self):
        self.clientes = [] # [] lista

    def cadastrar_cliente(self):

        while True: 
                nome = str(input(F"{CYAN}Nome: ")).strip() # strip  metodo que tira espaço do começo e do fim

                if nome == "": # == igualdade
                    print("O nome não pode ser vazio.") 

                elif not nome.isalpha(): #o metodo isdigit() verifica se o usuario digitou apenas numeros
                    print("Digite apenas letras para digitar seu nome")
                else:
                    break

        while True:
            try:
                idade = int(input("Idade: "))

                if idade <= 0 or idade == "": # or é u operador logico, serve para combinar condições
                    print("Idade inválida!")
                else:
                    break
            except ValueError:
                print("Digite apenas números")

        while True:  
            email = input("E-mail: ").strip()

            if "@" not in email: # se nao tiver o @ dentro//em email, vai dar errado
                    print("E-mail inválido! Insira o '@' no seu email")
            else:
                    break
            
        while True:
            
            telefone = input("Telefone: ").strip()

            if not telefone.isdigit(): #o metodo isdigit() verifica se o usuario digitou apenas numeros
                print("O telefone deve conter apenas números!")

            elif len(telefone) < 10: #se a quantidade de telefone for menor que 10, vai dar "erro"
                print("O telefone deve possuir pelo menos 10 dígitos!")

            else:
                break

        cliente = Cliente(nome, idade, email, telefone) # determinando a lista cliente é igual a nossa classe cliente (mesma coisa, atributos e tals)

        self.clientes.append(cliente) #adicionando os nossos clientes na nossa lista cliente

        self.salvar_arquivo(cliente)

        print("Cliente cadastrado com sucesso!")


    def listar_clientes(self):
        
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
                print(arquivo.read()) #o read () é um método que lê todo o conteudo do arquivo e devolve uma string (nesse caso, nossas informações)
                #nao pode so colocar print arquivo, pq se nao, ele exibe so objeto arquivo, e nao o conteudo. 
                
    def salvar_arquivo(self, cliente):


        with open(ARQUIVO, "a", encoding="utf-8") as arquivo: #open abre o arquivo, aarquivo é caminho. # a = adicionar coonteudo no final sem apagar oq ja existe
           #encoding = utf-8,permite salvar caracteres especiais
            arquivo.write(  #escreve um texto dentro do arquivo, no caso, oq esta abaixo
                f"Nome: {cliente.nome}\n"
                f"Idade: {cliente.idade}\n"
                f"E-mail: {cliente.email}\n"   #f: e uma forma de colocar variaveis dentro de um texto
                f"Telefone: {cliente.telefone}\n"
                f"{'--------------------------------------'}\n"
            )

    def menu(self):

        while True:

            print(f"{HOT_PINK} \n~~~~~~~~MENU PRINCIPAL~~~~~~~~~~ {RESET}")
            print(f"{PINK}1 - Cadastrar cliente{RESET}")
            print(f"{LIGHT_PINK}2 - Listar clientes{RESET}")
            print(f"{PINK}3 - Editar Cliente{RESET}")
            print(f"{LIGHT_PINK}4 - Ver cadastro atualizado{RESET}")  
            print(f"{HOT_PINK}5- Sair{RESET}")          
            print("--------------------------------")

            try:

                opcao = int(input("Escolha uma opção: "))

                if opcao == 1:
                    self.cadastrar_cliente()

                elif opcao == 2:
                    self.listar_clientes()

                elif opcao == 3:
                    print("Programa encerrado!")
                    break

                else:
                    print("Opção inválida!")

            except ValueError: #ValueError é um tipo de erro que ocorre quando um valor tem o tipo correto, mas é inválido para aquela operação.
                print("Digite apenas números!")

sistema = SistemaCadastro() #pra ela ser executada, temos que chamar a classe criada
sistema.menu() # objeto sistema exewcuta o método menu(), e vai mostrar as informações do menu