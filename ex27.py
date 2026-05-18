class produto:
    def __init__(self , nome ,preço):
        self.nome = nome
        self.preço = preço
        
    def mostrar (self):
        print(f"produto: {self.nome} | preço: {self.preço}")

p1 = produto("carros" , 5000)
p1.mostrar()
