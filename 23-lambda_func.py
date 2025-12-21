#FUNÇÃO LAMBDA TAMBÉM CONHECIDA COMO ANÔNIMA EM OUTRAS LINGUAGENS DE PROGRAMAÇÃO

#1 - Função de potência de um número
power = lambda num: num **2
print(power(5))
print(power(3))

#2 - Função que verifica se um número é par

is_even = lambda num : num %2 == 0 #Verifica se o resto da divisão do número é igual a 0

print(is_even(27))
print(is_even(30))

#3 - Função de divide um número por outro
div_num = lambda x,y : x / y

print(div_num(10,2))
print(div_num(10,5))

#4 - Função que inverte uma string
revert_string = lambda s : s[1:-1]#Tira uma letra do começo e outra do final
revert_string = lambda s : s[:]#Não tira nada nem do começo nem do final
revert_string = lambda s : s[::]#Não tira nada nem do começo nem do final
revert_string = lambda s : s[::-1]#Inverte todas as posições colocando a última na primeira até finalizar a string

print(revert_string("Python"))
print(revert_string("JavaScript"))

#5 - Funcionalidades relacionadas aos filmes:
#Lista de filmes
movie_list = ["Titanic", "The GodFather", "Inception", "Jurassic Park", "The Matrix"]
#Dicionario contendo as avaliações dos filmes
ratings = { 
    "Titanic":[8.5,9.3,6,8],
    "The GodFather":[9.5,5.3,7,8],
    "Inception":[6.5,7.3,8,8],
    "Jurassic Park":[7.5,8.3,5,8],
    "The Matrix":[8.1,9.2,6,6]
}
# Função para calcular a média de avaliações de um filme

average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])

#Dica extra
#Sempre que precisar colocar uma string dentro de outra, alterne entre aspas simples ' ' e aspas duplas " ". Isso evita conflitos de sintaxe.
print(f"A média de avaliação do filme Titanic é:{average_rating('Titanic'):.2f}")
print(f"A média de avaliação do filme The GodFather é:{average_rating('The GodFather'):.2f}")
print(f"A média de avaliação do filme Inception é:{average_rating('Inception'):.2f}")
print(f"A média de avaliação do filme Jurassic Park é:{average_rating('Jurassic Park'):.2f}")
print(f"A média de avaliação do filme The Matrix é:{average_rating('The Matrix'):.2f}")

# Função que verifica se um filme está na lista

check_movie = lambda movie_name : movie_name in movie_list
print(f"Inception está na lista? {check_movie('Inception')}")

# Função para recomendar um filme com base na avaliação média
recommend_movie = lambda movie_name : f"Recomendo assistir o filme {movie_name} com média de {average_rating(movie_name):.2f}"
#OBSERVAÇÃO -> :.2 arredonda o número, e :.2f exibe duas casas decimais
#Exemplo de saída
#Eu usei :.2 no código 
#recommend_movie = lambda movie_name : f"Recomendo assistir o filme {movie_name} com média de {average_rating(movie_name):.2}
#Saída -> Recomendo assistir o filme Titanic com média de 8.0
#Eu usei :.2f
#recommend_movie = lambda movie_name : f"Recomendo assistir o filme {movie_name} com média de {average_rating(movie_name):.2}
#Saída -> Recomendo assistir o filme Titanic com média de 7.95
print(f"{recommend_movie('Titanic')}")

