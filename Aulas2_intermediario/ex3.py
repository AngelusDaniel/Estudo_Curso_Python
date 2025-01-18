perguntas = [

  {
    "Pergunta": "Quanto é 2+2",
    "Opções": [1, 2, 3, 4],
    "Resposta": 4,
  },

  {
    "Pergunta": "Quanto é 5*3?",
    "Opções": [10, 15, 20, 25],
    "Resposta": 15,
  },

  {
    "Pergunta": "Quanto é 20/4",
    "Opções": [4, 5, 6, 8],
    "Resposta": 5,
  },

]

for pergunta in perguntas:
  print(pergunta["Pergunta"])

  opcoes = pergunta["Opções"]

  for index, opcao in enumerate(opcoes):
    print(f"Opção {index+1}: {opcao}")


  while True:
    resposta = input("\nInsira a resposta: \n")

    if(not resposta.isdigit()):
      print("Digite o número da opção. ")
      continue

    if(len(resposta)>1 or len(resposta)<=0):
      print("Digite apenas um número")
      continue

    if( int(resposta) > len(opcoes) or int(resposta) <=0):
      print("Digite um número dentre das opções. ")
      continue
    
    break

  resposta_int = int(resposta)
  

  if(pergunta["Resposta"] == opcoes[resposta_int-1]):
    print("\nResposta correta\n")
  else:
    print("\nResposta Incorreta\n")




