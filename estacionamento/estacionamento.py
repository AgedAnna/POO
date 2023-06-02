from main import Estacionamento


estacionamento = Estacionamento(10)  # Criando um estacionamento com 10 vagas

estacionamento.estacionar()  # Estacionando um veículo em uma vaga aleatória
estacionamento.verificar_vagas()  # Verificando as vagas disponíveis e ocupadas

estacionamento.pagar_estacionamento(3, 15.50)  # Pagando o estacionamento da vaga 3
estacionamento.verificar_caixa()  # Verificando o valor faturado e a quantidade de estacionamentos

estacionamento.retirar_veiculo(5)  # Removendo o veículo da vaga 5
estacionamento.verificar_vagas()  # Verificando as vagas disponíveis e ocupadas
