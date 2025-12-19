#Sets são coleções de elementos não-ordenados que não permite itens duplicados, ou seja, seus elementos são únicos como podemos ver no exemplo abaixo:
fimlsSet = {"Inception", "Interstellar", "The Dark Knight", 
            "Pulp Fiction", "Fight Club", "Forrest Gump"}

print(type(fimlsSet))

#1 Buscar o tamanho do set
print(len(fimlsSet))

#2 True e 1 são considerados os mesmo valor 
exemploSet = {"Pulp Fiction", "Fight Club", True, 1, 2, 8.9}
print(exemploSet)

#3 Adicionando um set dentro de outro set
fimlsSet.update(exemploSet)

print(fimlsSet) # Ele não mantém itens duplicados

#4 Remover um item dentro do set
print(len(fimlsSet))
fimlsSet.remove(True)
fimlsSet.remove(8.9)
fimlsSet.remove("Inception") # Se o item não existir, gera erro
print(len(fimlsSet))

#5 Sobre o método discard() - Remove um item do set, se o item não existir, não gera erro
fimlsSet.discard("Fight Club")
print(len(fimlsSet))

#6 Limpando o set
fimlsSet.clear()
print(len(fimlsSet))

#7 Verificando se um item está no set
print("Pulp Fiction" in fimlsSet)
print("The Dark Knight" in fimlsSet)

