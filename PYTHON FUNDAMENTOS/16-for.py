#LISTA DE FILMES

movieList = ["Star Wars", "Matrix", "Senhor dos Aneis", "Clube da Luta", "Forrest Gump"]

print(movieList)

#1 Iterando valores de uma lista

for movie in movieList:
    print(movie)


#2 Usando range para iterar sobre índices
for i in range(len(movieList)):
    print(f"{i} - {movieList[i]}")

print("-------------------------------")

#3 Quando a condição for atendida o loop será encerrado com break
for movie in movieList:
    if movie == "O Máskara":
        print("Achei o filme Clube da Luta!")
        break
else:
    print("Filme não encontrado na lista.")

#esse print retorna o valor do último item da lista no caso 'Forrest Gump'
print(len(movie))
        
#4 Quando a condição for atendida ele vai para a proxima iteração utilizando o comando continue
for movie in movieList:
    if movie == "Clube da Luta":
        continue #o comando continue faz pular o item que atende a condição, e não o imprime.
    print(movie)

print("-------------------------------")

#5 Programa avaliação do filme

filmName = input("Digite o nome do filme: ")
filmRange = int(input("Digite quantas avaliações deseja fazer"))

total = 0

for i in range(filmRange):
    nota = float(input("Digite a nota para o filme.\n"))
    total += nota

if nota > 0:
    average = total / filmRange
else:
    average = 0

print(f"A média de avalição do filme {filmName} é {average:.2f}")
# o :.2f formata o número para duas casas decimais






