#APRENDENDO FUNÇÃO EM PYTHON

#1 - Função para imprimir uma mensagem

def welcome(): #def palavra reservada para funções no python
    print("Bem vindos ao sistema de filmes :)")


##chamando a função
welcome()

for i in range(10):
    welcome()


#2 - Função para calcular média de notas
def calculate_average():
    num_ratings = int(input("Digite quantas avaliações deseja fazer para o filme:\n"))
    total = 0
    for i in range(num_ratings):
        note = int(input("Digite a nota que desejar para o filme\n"))
        total += note
    if num_ratings > 0:
        average  = total / num_ratings
    else:
        average = 0

    return average

#Chamando a função
print(f"A nota média do filme é :{calculate_average():.2f}")


#3 - Função para cadastrar um filme
def create_movie():
    name = input("Digite o nome  do filme:\n")
    yearLunch = int(input("Digite o ano de lançamento:\n"))
    moviePrice = float(input("Digite o valor do filme:\n"))
    rating = float(input("Digite a nota do filme:\n"))
    print(f"{name}, {yearLunch} R$ {moviePrice:.2f} {rating}")

create_movie()
create_movie()
