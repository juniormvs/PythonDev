"""
nome = input("Digite o nome do filme: \n")
ano = int(input("Digite o ano de lançamento do filme: \n"))
nota = float(input("Digite sua avaliação para o filme (0.0 - 10.0): \n"))

#
#ALETERNATIVA 1
print("Dados do filme: ")


print("===================================")
print("|| Nome do filme     ," , nome, "||")
print("|| Ano de lançamento ", ano, "  ||")
print("|| Nota do filme      ", nota, "  ||")
print("===================================")




#ALTERNATIVA 2
print("Nome do filme: ",nome, "\nAno de lançamento: ", ano, "\nNota do filme:", nota)

#ALETERNATIVA 3
print(f"Nome do filme: {nome}\n"
        f"Ano de lançamento: {ano}\n"
        f"Nota do filme: {nota}"
      )

"""


#TESTE
nome = input("digite seu nome:  \n")
print(f"Olá{nome}!")