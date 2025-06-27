from ex2banco import ContaBancaria

conta = ContaBancaria("Joao Silva")
conta.depositar(500)
conta.sacar(200)

print(conta.get_saldo())