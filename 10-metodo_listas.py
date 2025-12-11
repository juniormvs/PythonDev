films = ["Inception", "Interstellar", "The Dark Knight", "Pulp Fiction", "Fight Club", "Forrest Gump"]

#1 Tamanho da lista
print(len(films))  # 6

#2 Recuperar um item da lista pelo nome)
print(films.index("Pulp Fiction")) # 'Pulp Fiction'

#3 Adicionar um filme ao final da lista
films.append("The Matrix")
print(films)

#4 Ordenar a lista em ordem alfabética
films.sort()
print(films)

#5 Copiar os itens de uma lista para outra
filmsCopy = films.copy()
print(filmsCopy)

#6 Remover um item da lista pelo nome
filmsCopy.remove("Fight Club")
print(filmsCopy)

#7 Inverter a ordem dos itens na lista
filmsCopy.reverse()
print(filmsCopy)

#8 Remove todos os itens da lista
filmsCopy.clear()
print(filmsCopy)  # []

#9 Verificar se um item está na lista
print("Inception" in films)  # True