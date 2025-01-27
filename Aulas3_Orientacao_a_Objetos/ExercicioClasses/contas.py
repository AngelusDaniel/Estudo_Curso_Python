import abc
class Conta(abc.ABC):
  
  def __init__(self, agencia: int, conta: int, saldo:float =0):
    self.agencia = agencia
    self.conta = conta
    self.saldo = saldo

  @abc.abstractmethod
  def sacar(self, valor) -> None: ...


  def depositar(self, valor: float) -> float:
    self.saldo += valor
    self.detalhes(f"Depósito realizado {valor}")
    return self.saldo


  def detalhes(self, msg: str ="") -> None: 
    print(f"{msg}, O seu saldo é: {self.saldo:.2f}")



class ContaPoupanca(Conta):

  def sacar(self, valor: float) -> float:
    valor_pos_saque = self.saldo - valor
    if valor_pos_saque  < 0:
      self.detalhes("Saldo insuficiente")
      return self.saldo
    self.saldo = valor_pos_saque
    self.detalhes(f"Você sacou {valor}")
    return self.saldo

class ContaCorrente(Conta):
  def __init__(self, agencia:int, conta:int, saldo:float =0, limite:float =0):
    super().__init__(agencia, conta, saldo)
    self.limite = limite  

  def sacar(self, valor: float) -> float:
    valor_pos_saque = self.saldo - valor
    limite_maximo = -self.limite

    if valor_pos_saque < limite_maximo:
      self.detalhes("Saldo e Limite insuficiente")
      return self.saldo
    
    self.saldo = valor_pos_saque
    self.detalhes(f"Você sacou {valor}")
    return self.saldo


if __name__ == "__main__":
  conta1 = ContaPoupanca(32433432332, 3232, 1000)

  conta1.sacar(600)
  conta1.depositar(300)

  print("------------------")
  conta2 = ContaCorrente(111, 222, 0, 100)
  conta2.depositar(1)
  conta2.sacar(50)
  conta2.sacar(120)





