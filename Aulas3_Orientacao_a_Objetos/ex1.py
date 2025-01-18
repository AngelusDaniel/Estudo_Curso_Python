

class Carro:
  def __init__(self, modelo):
    self.modelo = modelo
    self._motor = None
    self._fabricante = None

  # def inserir_motor(self, motor):
  #   self.motor = motor

  @property
  def motor(self):
   return self._motor
  
  @motor.setter
  def motor(self, value):
    self._motor = value


  @property
  def fabricante(self):
   return self._fabricante
  
  @fabricante.setter
  def fabricante(self, value):
    self._fabricante = value

  def carro_tem_motor(self):
    print(f"O carro {self.modelo} tem o motor {self.motor}")

  def carro_tem_fabricante(self):
    print(f"O carro {self.modelo} é da fabricante {self.fabricante}")



class Motor:
  def __init__(self, nome):
    self.nome = nome


class Fabricante:
  def __init__(self, nome):
    self.nome = nome



porshe_tal = Carro("Porsche tal")

motor_v6 = Motor("Motor V6")

porshe = Fabricante("Porsche")

porshe_tal.motor = motor_v6
porshe_tal.fabricante = porshe

print(porshe_tal.fabricante.nome)
print(porshe_tal.motor.nome)

