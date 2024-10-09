class Pessoa:
    def __init__(self, nome, peso,idade):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.statusAndar = False
        self.statusComer = False
        self.statusDormir = False

    def andar(self):
        if self.statusAndar == False:
            print(f"{self.nome} foi andar")
            self.statusAndar = True
        elif:
            self.statusAndar = True
            print("Você não pode comer e nem dormir")
        else:
           print(f"{self.nome} já está andando")
    def comer(self):
        if self.statusComer == False:
            print(f"{self.nome} foi comer")
            self.statusComer = True
        else:
            print(f"{self.nome} já está andando")
    def dormir(self):
        if self.statusDormir == False:
            print(f"{self.nome} foi dormir")
            self.statusDormir = True
        else:
            print(f"{self.nome} já está dormindo")


