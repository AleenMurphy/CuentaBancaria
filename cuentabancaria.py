class CuentaBancaria:
    tasa_interes = 0.01
    cuentas = []  # Inicializamos la lista de cuentas

    def __init__(self, balance=0):
        self.balance = balance
        self.cuentas.append(self)  # Agregamos la instancia a la lista de cuentas

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if amount > self.balance:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance}")
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interes
        return self

    @classmethod
    def imprimir_todas_las_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()

cuenta1 = CuentaBancaria(1000)
cuenta2 = CuentaBancaria()

cuenta1.deposito(200).deposito(300).deposito(500).retiro(150).generar_interes().mostrar_info_cuenta()

cuenta2.deposito(300).deposito(400).retiro(50).retiro(100).retiro(200).retiro(100).generar_interes().mostrar_info_cuenta()

CuentaBancaria.imprimir_todas_las_cuentas()

