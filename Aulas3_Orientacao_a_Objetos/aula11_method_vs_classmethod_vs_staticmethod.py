#method - self, método de instância
#classmethod - cls, método de classe
#staticmethod - método estático (sem self e sem cls)
#toda vez que precisar usar self, este método é um metodo de instância

class Connection:
  def __init__(self, host="localhost"):
    self.host = host
    self.user = None
    self.password = None
  
  def set_user(self, user):
    #setter
    self.user = user

  def set_password(self, password):
    self.password = password

  @classmethod
  def create_with_auth(cls, user, password):
    connection = cls()
    connection.user = user
    connection.password = password
    return connection
  

  @staticmethod
  def log(msg):
    print(f"LOG: {msg}")


#c1 = Connection()
c1 = Connection.create_with_auth("Daniel", "123")
# c1.set_user("Daniel")
# c1.set_password("Teste123")
Connection.log("mensagem log")
print(c1.user)
print(c1.password)
