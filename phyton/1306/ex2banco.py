class ContaBancaria:
    def __init__(self , __titular):

        self.__saldo = 0.0
        self.__titular = __titular

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor


    def get_saldo(self):
        return self.__saldo
