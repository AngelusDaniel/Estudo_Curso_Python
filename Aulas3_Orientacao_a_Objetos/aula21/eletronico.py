from log import LogPrintMixin

class Eletronico:
  def __init__(self, nome):
    self._nome = nome
    self._ligado = False

  def ligar(self):
    if not self._ligado:
      self._ligado = True

  def desligar(self):
    if self._ligado:
      self._ligado = False



class Smartphone(Eletronico, LogPrintMixin):
  # def __init__(self, nome):
  #   super().__init__(nome) #mantém o init do Eletronico
  #   self._log = LogPrintMixin()  #Usando associação, sem usar herança multipla / EX poderia usar em ligar self._log.log_success("Ligado com sucesso")

  def ligar(self):
    super().ligar() #mantém a funcionalidade

    if self._ligado:
      self.log_success(f"{self._nome} Ligado com sucesso")


  def desligar(self):
    super().desligar()

    if not self._ligado:
      self.log_error(f"{self._nome} Desligado")

