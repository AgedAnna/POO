import random

class Estacionamento:
    def __init__(self, quantidade_vagas):
        self.quantidade_vagas = quantidade_vagas
        self.vagas_livres = list(range(1, quantidade_vagas + 1))
        self.vagas_ocupadas = []
        self.valor_faturado = 0
        self.quantidade_estacionamentos = 0

    def estacionar(self):
        if not self.vagas_livres:
            print("Não há vagas disponíveis.")
            return

        vaga = random.choice(self.vagas_livres)
        self.vagas_livres.remove(vaga)
        self.vagas_ocupadas.append(vaga)
        self.quantidade_estacionamentos += 1
        print(f"Veículo estacionado na vaga {vaga}.")

    def retirar_veiculo(self, vaga):
        if vaga not in self.vagas_ocupadas:
            print(f"A vaga {vaga} não está ocupada.")
            return

        self.vagas_ocupadas.remove(vaga)
        self.vagas_livres.append(vaga)
        print(f"Veículo removido da vaga {vaga}.")

    def verificar_caixa(self):
        print(f"Valor faturado: R${self.valor_faturado:.2f}")
        print(f"Quantidade de estacionamentos realizados: {self.quantidade_estacionamentos}")

    def verificar_vagas(self):
        print(f"Vagas disponíveis: {self.vagas_livres}")
        print(f"Vagas ocupadas: {self.vagas_ocupadas}")

    def pagar_estacionamento(self, vaga, valor):
        if vaga not in self.vagas_ocupadas:
            print(f"A vaga {vaga} não está ocupada.")
            return

        self.valor_faturado += valor
        self.retirar_veiculo(vaga)

