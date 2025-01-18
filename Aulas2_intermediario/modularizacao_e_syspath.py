
try: 
  import sys
  sys.path.append("/home/daniel/Área de trabalho") #se eu criar um arquivo no desktop por exemplo e incluir o caminho do desktop, eu consigo usar o modulo

except ModuleNotFoundError:
  ...

import modularizacao_import
import import_modulo #do desktop mas evitar 

print("Este módulo se chama", __name__)
print(*sys.path, sep="\n")





