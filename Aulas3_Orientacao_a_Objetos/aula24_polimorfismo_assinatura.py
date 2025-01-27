#SO"L"ID
#Princípio da substituição de liskov

#Sobreposição de métodos(Override)

from abc import ABC, abstractmethod

class Notificacao(ABC):
  def __init__(self, mensagem):
    self.mensagem = mensagem

  @abstractmethod
  def enviar(self) -> bool:
    ...

class NotificacaoEmail(Notificacao):
  
  def enviar(self):
    print("E-mail: enviando: ", self.mensagem)
    return True

class NotificacaoSms(Notificacao):
  
  def enviar(self):
    print("SMS: enviando: ", self.mensagem)
    return True



def notificar(notificacao: Notificacao):
  notificacao_enviada = notificacao.enviar()

  if notificacao_enviada:
    print("Notificação enviada")
  else:
    print("Notificação não enviada")

notificacao_email = NotificacaoEmail("Testando")
notificar(notificacao_email)
notificar(NotificacaoSms("Testando"))