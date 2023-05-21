class Pessoa:
    def __init__(self,nome, idade, falando=False, comendo=False):

        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comedo = comendo

    def comer(self, alimento):
        if self.comedo:
            print("Já está comendo")
            return

        if self.comedo==False:
            print(f"{self.nome} começou a comer {alimento}")

        else:
            print(f"{self.nome} já está comendo {alimento}")
            self.comedo == True


