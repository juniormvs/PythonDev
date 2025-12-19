#Se convenciona que listas são para item homogêneos (tudo inteiro, tudo string etc).
#Mas nada impede de criar listas com itens heterogêneos (diferentes tipos de dados).

filmeMatrix = ["Matrix", "Matrix ", "1999", 8.7, True]
print(type(filmeMatrix))  # <class 'list'>
print(filmeMatrix)

#====================================================

films = ["Inception", "Interstellar", "The Dark Knight", "Pulp Fiction", "Fight Club", "Forrest Gump"]
print(films)  # Acessa a lista completa

# Acessar o primeiro filme da lista
print(films[0]) # 'Inception'

# Acessar o terceiro filme da lista
print(films[2]) # 'The Dark Knight'

# Buscar os dois primeiros filmes da lista
print(films[:2])  # ['Inception', 'Interstellar'] ele pega o índice 0 e 1

# Buscar o último filme da lista
print(films[-1]) # 'Forrest Gump'

# Buscar os três últimos filmes da lista
print(films[-3:])  # ['Fight Club', 'Forrest Gump'] pega o índice -3, -2 e -1
# Buscar filmes do índice 1 ao 3 (exclui o índice 4)
print(films[1:4])  # ['Interstellar', 'The Dark Knight', 'Pulp Fiction']