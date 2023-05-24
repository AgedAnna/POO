class ContaBancaria:
    def __init__(self, tipo, nome, numero, saldo, limite, status_conta=True):

        self.tipo = tipo
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
        self.status_conta=status_conta

    def ativar_conta(self):
        if not self.status_conta:
            self.status_conta = True
            print("Conta Ativada")
        else:
            print("Conta desativada")

    def depositar(self, valor):
        if self.status_conta == True:
            if valor > 0:
                self.saldo+=valor
                print("Depósito realizado com sucesso")

            else:
                print("Depósito inválido")

    def sacar(self, valor):
        if self.status_conta == True:
            if valor > 0 and valor >= self.saldo:
                self.saldo-=-valor
                print(f"Saque realizado com sucesso")

            else:
                print("Saque indisponível")

    def verificar_saldo(self):
        print(f"Saldo atual da conta: {self.saldo}")
