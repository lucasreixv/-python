class Cliente:
    def __init__ (self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
    
    def mostrar(self):
            print(f"{self.nome} | {self.idade} | {self.email} | {self.telefone}")

clientes =  []

def cadastrar_cliente():
    while True:
        nome = input("Digite seu nome: ").strip().lower()
        # Verifica se está vazio
        if not nome: #se nome for vazio ou equivalente a falso, ou seja, se nao tiver nada no nome, ele entra no if
            print("  nome não pode estar vazio. Tente novamente.")
            continue
              
        try: #tratamento de erro, TENTE ISSO

            idade = int(input("Idade: ").strip()) #Pedir o preço pro usuario
            
            if idade <=0: #se o preço for esse valor, invalido
                print("idade inválida!")

            else:
                cliente = Cliente(nome, idade) #se nao, o nosso produto vira o produto da classe, com nome e preço
                clientes.append(cliente)  #colocando nosso produto dentro da lista

                print("Cliente cadastrado!")
                
        except ValueError: #exceção, erro, vai pedir dnv
            print("Erro! Digite valores válidos.")



def listar_clientes():
    if len(clientes) <=0:
        print("Nenhum cliente cadastrado!")
    else:
        for i in range(len(clientes)): #percorre o indice em um raio de quantidade da lista produtos
            cliente = clientes[i] #produto = lista de produtos na posição que ela esta
            cliente.mostrar()

#MOSTRAR

while True:
    while True:
        print("\nMENU DO USUÁRIO:")
        print("1 - Cadastro de Cliente(s)")
        print("2 - Listar clientes")
        print("3 - Sair")
        
        try:
            
          opção = int(input("Escolha uma opção: "))
        
          if opção == 1:
              cadastrar_cliente()
                
          elif opção == 2:
                listar_clientes()
                
          elif opção == 3:
                print("Programa encerrado ! ")
            
        except ValueError:
            print("Digite apenas números!")