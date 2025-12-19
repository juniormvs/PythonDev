#UTILIZANDO LISTCOMPREHENTION

#exemplo simples com for
'''
for i in range(10):
    if i < 4 :
        print(i)

'''

listNumber = [i for i in range(10)]
print(listNumber)

#1 Listando valores de 0 -10 que sejam menores do que 4
listNumber = [i for i in range(20) if i < 4]
print(listNumber)

#LISTA DE FILMES

#PROGRAMA SIMPLES DE BUSCA DE FILMES, ITEMS, DENTRO DE UMA LISTCOMPREHENTION

movieList = ["Star Wars", "Matrix", "Senhor dos Aneis", "Clube da Luta", "Forrest Gump"]

#2 Filmes que possuem a letra 'e' no título
moviesWithE = [movie for movie in movieList if 'e' in movie.lower()] #convertendo tudo para minusculo e procurando filmes que possuema letra 'e'
print(moviesWithE)


#3 Filmes que eu assisti
moviesWatched = [movie for movie in movieList if movie != 'Clube da Luta' and movie != 'Forrest Gump']
print(moviesWatched)

#4 Encontrando um filme pelo nome

while True:
    searchName = input("Digite o nome do filme para buscar na lista (ou sair para encerrar):\n")
    if searchName.lower() == "sair":
        print("Encerrar o programa!")
        break

    foundMovies = [movie for movie in movieList if searchName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filmes encontrados com o nome: {searchName}:" )
        for foundMovie in foundMovies:
            print(foundMovie)
    else:
        print(f"Nenhum filme foi encontrado com o nome {searchName}. Tente novamente!")



                
        
