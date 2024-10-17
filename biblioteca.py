class Pessoa:
    def __init__(self, nome, peso,idade):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo = False
        self.andando = False
        self.dormindo = False
    def parar(self):
        self.comendo = False
        self.andando = False
        self.dormindo = False
        print(f"{self.nome} parou")
    def comer(self):
        if self.comendo == False:
            if self.andando == False:
                if self.dormindo == False:
                    print(f"{self.nome} foi comer")
                    self.comendo = True
                else:
                    print(f"{self.nome} não foi comer porque está dormindo")
            else:
                print(f"{self.nome} não foi andar porque está dormindo")
        else:
            print(f"{self.nome} já está comendo")

    def andar(self):
        if self.andando == False:
            if self.comendo == False:
                if self.dormindo == False:
                    print(f"{self.nome} foi andar")
                    self.andando = True
                else:
                    print(f"{self.nome} não foi andar porque está dormindo")
            else:
                print(f"{self.nome} não foi andar porque está comendo")
        else:
            print(f"{self.nome} ja está andando")

    def dormir(self):
        if self.dormindo == False:
            if self.andando == False:
                if self.comendo == False:
                    print(f"{self.nome} foi dormir")
                    self.dormindo = True
                else:
                    print(f"{self.nome} não foi  dormir porque está comendo")
            else:
                print(f"{self.nome} não foi dormir porque está andando")
        else:
            print(f"{self.nome} ja está dormindo")

class Animal:
    def __init__(self, nome, cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
       print(f"O {self.nome} foi comer...")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def miar(self):
        print(f"O {self.nome} foi miando")

class Cachorro(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome, cor)
    def latir(self):
        print(f"O {self.nome} fez AU AU")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def pular(self):
        print(f"O {self.nome} foi pulando")













