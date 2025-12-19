#LISTA DE FILMES

movieList = ["Star Wars", "Matrix", "Senhor dos Aneis", "Clube da Luta", "Forrest Gump"]

#1 Iterando uma lista de filmes usando o comando while



'''
index = 0
while index < len(movieList):
    print(movieList[index])
    index += 1


'''

'''
#2 Quando a condição for atendida o loop será encerrado
index = 0
while index < len(movieList):
    if movieList[index] == "Clube da Luta":
        break
    print(movieList[index])
    index += 1
'''

#3 Quando a condição for atendida, o loop vai para a próxima iteração, utilizando o comando continue

index = 0
while index < len(movieList):
    if movieList[index] == "Senhor dos Aneis":
        index += 1
        continue
    print(movieList[index])
    index += 1

#4 Avaliação do filme utilizando while

movieName = input("Digite o nome do filme: ")
movieRating = int(input("Digite quantas avaliações deseja fazer"))
total = 0
count = 0


while count < movieRating :
    note = float(input("Digite a nota para o filme:\n"))
    total += note
    count += 1

if movieRating > 0 :
    average = total / movieRating
else:
    tota = 0
    
print(f"Média de avaliação do filme {movieName} é {average:.2f}")
