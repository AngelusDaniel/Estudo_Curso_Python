
#agregacao - é uma forma mais especializada de associação entre dois ou mais objetos.
#cada objeto terá seu ciclo de vida independente
#Geralmente é uma relação de um para muitos


class Carrinho:
  def __init__(self):
    self._produtos = []


  def total(self):
    return sum([p.preco for p in self._produtos])
  
  def listar_produtos(self):
    for produto in self._produtos:
      print(produto.nome, produto.preco)
    print()

  # def inserir_produtos_no_carrinho(self, *produtos):
  #   print(produtos)
  #   for produto in produtos:
  #     self._produtos.append(produto)

  def inserir_produtos_no_carrinho(self, *produtos):
    #self._produtos.extend(produtos)
    self._produtos += produtos



class Produto:
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco


carrinho = Carrinho()
# p1 = Produto("Caneta", 1.20)
# p2 = Produto("Camiseta", 20)
p1, p2 = Produto("Caneta", 1.20), Produto("Camiseta", 20)

carrinho.inserir_produtos_no_carrinho(p1, p2)

carrinho.listar_produtos()

print(carrinho.total())


