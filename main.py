from banco import ContaBancaria

conta1 = ContaBancaria("corrente", "anna", "899", 1500,1000)

conta1.depositar(10)
conta1.verificar_saldo()

conta1.sacar(300)
conta1.verificar_saldo()

