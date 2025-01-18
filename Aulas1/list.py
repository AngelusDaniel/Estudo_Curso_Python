

string = "ABCD"

lista = ["teste", "daniel", 1, 2, 3, 4]

lista2 = ['um', "dois", "três"]

#del lista[3] #evite del itens no meio da lista em listas grandes requer muito processamento

lista.append(1) #add no final

lista.append("lul")

lista.pop() #deleta final

ultimo_valor = lista.pop();

lista.insert(4, "add") #add elemento em determinado indicie, evitar usar sem ser no final

lista.insert(100,9)

print(lista, ultimo_valor)

#clear - limpa a lista

lista3 = lista + lista2;

lista.extend(lista2)

print(lista3, lista)


#PARA COPIAR Lista use lista.copy()


